from abc import abstractmethod
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, ClassVar, TypedDict
from typing_extensions import Unpack

from ._distutils.cmd import Command as _Command
from .depends import Require as Require
from .discovery import _Path
from .dist import Distribution as Distribution
from .extension import Extension as Extension
from .warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

# https://setuptools.pypa.io/en/latest/references/keywords.html
class _SetupKeywords(TypedDict, total=False):
    name: str
    version: str
    description: str
    long_description: str
    long_description_content_type: str
    author: str
    author_email: str
    maintainer: str
    maintainer_email: str
    url: str
    download_url: str
    packages: Sequence[str]
    py_modules: Sequence[str]
    scripts: Sequence[str]
    ext_package: str
    ext_modules: Sequence[Extension]
    classifiers: str | list[str]  # can be comma-separated list string
    distclass: type[Distribution]
    script_name: str
    script_args: Sequence[str]
    options: Mapping[str, Any]
    license: str
    license_file: str  # deprecated by license_files
    license_files: Sequence[str]
    keywords: str | list[str]  # can be comma-separated list string
    platforms: str | list[str]  # can be comma-separated list string
    cmdclass: Mapping[str, type[Command]]
    data_files: Sequence[tuple[str, Sequence[str]]]  # DISCOURAGED
    package_dir: Mapping[str, str]
    requires: Sequence[str]  # superseded by install_requires
    obsoletes: Sequence[str]  # ignored by pip
    provides: Sequence[str]  # ignored by pip
    include_package_data: bool
    exclude_package_data: Mapping[str, Sequence[str]]
    package_data: Mapping[str, Sequence[str]]
    zip_safe: bool
    install_requires: str | Sequence[str]
    entry_points: Mapping[str, str | Sequence[str]]
    extras_require: Mapping[str, str | Sequence[str]]
    python_requires: str
    setup_requires: Sequence[str]  # discouraged in favor of PEP 518
    dependency_links: Sequence[str]  # deprecated. Not supported anymore by pip
    namespace_packages: Sequence[str]  # deprecated in favor of native/implicit namespaces (PEP 420)
    test_suite: str  # Deprecated since version 41.5.0
    tests_require: str | Sequence[str]  # Deprecated since version 41.5.0
    test_loader: str  # Deprecated since version 41.5.0
    eager_resources: Sequence[str]
    project_urls: Mapping[str, str]

__all__ = [
    "setup",
    "Distribution",
    "Command",
    "Extension",
    "Require",
    "SetuptoolsDeprecationWarning",
    "find_packages",
    "find_namespace_packages",
]

__version__: str

# Pytype fails with the following:
# find_packages = PackageFinder.find
# find_namespace_packages = PEP420PackageFinder.find
def find_packages(where: _Path = ".", exclude: Iterable[str] = (), include: Iterable[str] = ("*",)) -> list[str]: ...
def find_namespace_packages(where: _Path = ".", exclude: Iterable[str] = (), include: Iterable[str] = ("*",)) -> list[str]: ...
def setup(**attrs: Unpack[_SetupKeywords]) -> None: ...

class Command(_Command):
    command_consumes_arguments: ClassVar[bool]
    def __init__(self, dist: Distribution, **kw: Any) -> None: ...
    def ensure_string_list(self, option: str | list[str]) -> None: ...
    def reinitialize_command(self, command: _Command | str, reinit_subcommands: int = 0, **kw: Any) -> _Command: ...
    @abstractmethod
    def initialize_options(self) -> None: ...
    @abstractmethod
    def finalize_options(self) -> None: ...
    @abstractmethod
    def run(self) -> None: ...

class sic(str): ...
