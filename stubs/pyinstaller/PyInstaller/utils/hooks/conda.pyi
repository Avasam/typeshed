# https://pyinstaller.org/en/stable/hooks.html?highlight=conda_support#module-PyInstaller.utils.hooks.conda

import sys
from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from pathlib import Path, PurePath
from typing import Any
from typing_extensions import TypeAlias, TypedDict

if sys.version_info >= (3, 8):
    from importlib.metadata import PackagePath as _PackagePath
else:
    _PackagePath: TypeAlias = Any

CONDA_ROOT: Path
CONDA_META_DIR: Path
PYTHONPATH_PREFIXES: list[Path]

class _RawDict(TypedDict):
    name: str
    version: str
    files: list[StrOrBytesPath | PurePath]
    depends: list[str]

class Distribution:
    raw: _RawDict
    name: str
    version: str
    files: list[PackagePath]
    dependencies: list[str]
    packages: list[str | None]
    def __init__(self, json_path: str) -> None: ...
    @classmethod
    def from_name(cls, name: str) -> Distribution: ...
    @classmethod
    def from_package_name(cls, name: str) -> Distribution: ...

class PackagePath(_PackagePath):
    def locate(self) -> Path: ...

def walk_dependency_tree(initial: str, excludes: Sequence[str] | None = ...) -> dict[str, Distribution]: ...
def requires(name: str, strip_versions: bool = ...) -> list[str]: ...
def files(name: str, dependencies: bool = ..., excludes: Sequence[str] | None = ...) -> list[PackagePath]: ...
def collect_dynamic_libs(
    name: str, dest: str = ..., dependencies: bool = ..., excludes: Sequence[str] | None = ...
) -> list[tuple[str, str]]: ...

distributions: dict[str, Distribution]
distributions_by_package: dict[str | None, Distribution]
