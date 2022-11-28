"""Utility to load and parse METADATA.toml."""
from __future__ import annotations

import os
import re
from typing import Any, cast
from typing_extensions import Literal, TypedDict

import tomli
from packaging.requirements import Requirement
from packaging.version import Version

# Used to install system-wide packages for different OS types:
METADATA_MAPPING: dict[str, Literal["apt_dependencies", "brew_dependencies", "choco_dependencies"]] = {
    "linux": "apt_dependencies",
    "darwin": "brew_dependencies",
    "win32": "choco_dependencies",
}

metadata_keys = {
    "version",
    "requires",
    "extra_description",
    "stub_distribution",
    "obsolete_since",
    "no_longer_updated",
    "upload",
    "tool",
}

tool_keys = {
    "stubtest": {
        "skip",
        "apt_dependencies",
        "brew_dependencies",
        "choco_dependencies",
        "extras",
        "ignore_missing_stub",
        "platforms",
    }
}
supported_stubtest_platforms = {"win32", "darwin", "linux"}
dist_name_re = re.compile(r"^[a-z0-9]([a-z0-9._-]*[a-z0-9])?$", re.IGNORECASE)


class MetaDataToolStubtestDict(TypedDict):
    platforms: set[str]
    apt_dependencies: list[str]
    brew_dependencies: list[str]
    choco_dependencies: list[str]
    # TODO: items below are not type validated
    skip: bool
    ignore_missing_stub: bool
    extras: list[str]


class MetaDataToolDict(TypedDict):
    stubtest: MetaDataToolStubtestDict


class MypySectionDict(TypedDict):
    module_name: str
    values: dict[str, dict[str, Any]]


_MetaDataMypyDict = TypedDict("_MetaDataMypyDict", {"mypy-tests": dict[str, MypySectionDict]})


class MetaDataDict(_MetaDataMypyDict):
    version: Version
    requires: list[Requirement]
    stub_distribution: str
    upload: bool
    tool: MetaDataToolDict


def validate_metadata(metadata: dict[str, Any], distribution: str | os.PathLike[str]) -> MetaDataDict:
    # MetaDataDict.*
    for key in metadata:
        assert key in metadata_keys, f"Unexpected key {key} for {distribution}"

    # MetaDataDict.version
    assert "version" in metadata, f"Missing version for {distribution}"
    version = metadata["version"]
    assert isinstance(version, str), f"Unsupported version {repr(version)}"
    # Check that the version parses
    metadata["version"] = Version(version.removesuffix(".*"))

    # MetaDataDict.requires
    metadata_requires: list[str] | None = metadata.get("requires")
    if metadata_requires is None:
        metadata["requires"] = metadata_requires = []
    else:
        assert isinstance(metadata_requires, list), f"Invalid requires value for {distribution}"

    # MetaDataDict.requires[*]
    for i, dep in enumerate(metadata_requires):
        assert isinstance(dep, str), f"Invalid requirement {repr(dep)} for {distribution}"
        assert dep.startswith("types-"), f"unrecognized dependency {dep!r}"
        for space in " \t\n":
            assert space not in dep, f"For consistency, requirement should not have whitespace: {dep}"
        # Check that the requirements parses
        metadata["requires"][i] = Requirement(dep)

    # MetaDataDict.stub_distribution
    if "stub_distribution" in metadata:
        assert dist_name_re.fullmatch(metadata["stub_distribution"]), f"Invalid 'stub_distribution' value for {distribution!r}"

    # MetaDataDict.upload
    metadata_upload: bool | None = metadata.get("upload")
    if metadata_upload is None:
        metadata["upload"] = metadata_upload = True
    else:
        assert isinstance(metadata_upload, bool), f"Invalid 'upload' value for {distribution!r}"

    # MetaDataDict.tool
    metadata_tool: dict[str, dict[str, Any]] | None = metadata.get("tool")
    if metadata_tool is None:
        metadata["tool"] = metadata_tool = {}
    else:
        assert set(metadata_tool).issubset(tool_keys.keys()), f"Unrecognised tool for {distribution}"

    # MetaDataDict.tool.*
    for tool, tk in tool_keys.items():
        metadata_tool_tool = metadata_tool.get(tool)
        if metadata_tool_tool is None:
            metadata["tool"][tool] = metadata_tool_tool = {}
        else:
            # MetaDataDict.tool.*.*
            for key in metadata_tool_tool:
                assert key in tk, f"Unrecognised {tool} key {key} for {distribution}"

    # MetaDataDict.tool.stubtest
    metadata_tool_stubtest = metadata_tool["stubtest"]

    # MetaDataDict.tool.stubtest.platforms
    metadata_tool_stubtest_platforms = set(metadata_tool_stubtest.get("platforms", []))
    metadata["tool"]["stubtest"]["platforms"] = metadata_tool_stubtest_platforms
    assert (
        metadata_tool_stubtest_platforms <= supported_stubtest_platforms
    ), f"Unrecognised platforms specified: {supported_stubtest_platforms - metadata_tool_stubtest_platforms} for {distribution}"

    # MetaDataDict.tool.stubtest.*_dependencies
    # Check that os packages are only installed for specified platforms:
    for supported_platform in supported_stubtest_platforms:
        if supported_platform not in metadata_tool_stubtest_platforms:
            assert (
                METADATA_MAPPING[supported_platform] not in metadata_tool_stubtest
            ), f"Installing system deps for unspecified platform {supported_platform} for {distribution}"
    for dependency_key in METADATA_MAPPING.values():
        dependencies = metadata_tool_stubtest.get(dependency_key)
        if dependencies is None:
            metadata_tool_stubtest[dependency_key] = []
        else:
            assert isinstance(dependencies, list), f"Invalid {dependency_key} value for {distribution!r}"
            # MetaDataDict.tool.stubtest.*_dependencies[*]
            for dependency in dependencies:
                assert isinstance(dependency, str), f"Invalid {dependency_key} dependency {dependency} for {distribution!r}"

    # MetaDataDict.tool.stubtest.skip
    metadata_tool_stubtest_skip: bool | None = metadata_tool_stubtest.get("skip")
    if metadata_tool_stubtest_skip is None:
        metadata["tool"]["stubtest"]["skip"] = metadata_tool_stubtest_skip = False
    else:
        assert isinstance(metadata_tool_stubtest_skip, bool), f"Invalid 'skip' value for {distribution!r}"

    # MetaDataDict.tool.stubtest.ignore_missing_stub
    metadata_tool_stubtest_ignore_missing_stub: bool | None = metadata_tool_stubtest.get("ignore_missing_stub")
    if metadata_tool_stubtest_ignore_missing_stub is None:
        metadata["tool"]["stubtest"]["ignore_missing_stub"] = metadata_tool_stubtest_ignore_missing_stub = True
    else:
        assert isinstance(
            metadata_tool_stubtest_ignore_missing_stub, bool
        ), f"Invalid 'ignore_missing_stub' value for {distribution!r}"

    # MetaDataDict.tool.stubtest.extras
    metadata_tool_stubtest_extras: list[str] | None = metadata_tool_stubtest.get("extras")
    if metadata_tool_stubtest_extras is None:
        metadata["tool"]["stubtest"]["extras"] = metadata_tool_stubtest_extras = []
    else:
        assert isinstance(metadata_tool_stubtest_extras, list), f"Invalid 'extras' value for {distribution!r}"

    # MetaDataDict.tool.stubtest.extras[*]
    for extra in metadata_tool_stubtest_extras:
        assert isinstance(extra, str), f"Invalid extra {extra} for {distribution!r}"

    # MetaDataDict.mypy-tests
    metadata_mypy_tests: dict[str, dict[str, dict[str, dict[str, Any]]]] | None = metadata.get("mypy-tests")
    if metadata_mypy_tests is None:
        metadata["mypy-tests"] = metadata_mypy_tests = {}
    else:
        assert isinstance(metadata_mypy_tests, dict), "mypy-tests should be a section"

    # MetaDataDict.mypy-tests.*
    for section_name, mypy_section in metadata_mypy_tests.items():
        assert isinstance(mypy_section, dict), f"{section_name} should be a section"
        module_name = mypy_section.get("module_name")

        assert module_name is not None, f"{section_name} should have a module_name key"
        assert isinstance(module_name, str), f"{section_name} should be a key-value pair"

        values = mypy_section.get("values")
        assert values is not None, f"{section_name} should have a values section"
        assert isinstance(values, dict), "values should be a section"

    return cast(MetaDataDict, metadata)


def load_metadata(distribution: str | os.PathLike[str]) -> MetaDataDict:
    with open(os.path.join("stubs", distribution, "METADATA.toml"), encoding="UTF-8") as file:
        metadata = tomli.loads(file.read())
    return validate_metadata(metadata, distribution)
