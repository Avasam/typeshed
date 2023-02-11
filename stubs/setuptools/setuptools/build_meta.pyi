from _typeshed import Incomplete
from typing import Any
from typing_extensions import Final

from setuptools import dist

__all__ = [
    "get_requires_for_build_sdist",
    "get_requires_for_build_wheel",
    "prepare_metadata_for_build_wheel",
    "build_wheel",
    "build_sdist",
    "get_requires_for_build_editable",
    "prepare_metadata_for_build_editable",
    "build_editable",
    "__legacy__",
    "SetupRequirementsError",
]

SETUPTOOLS_ENABLE_FEATURES: Final[str]
LEGACY_EDITABLE: Final[bool]

class SetupRequirementsError(BaseException):
    specifiers: Any
    def __init__(self, specifiers) -> None: ...

class Distribution(dist.Distribution):
    def fetch_build_eggs(self, specifiers) -> None: ...
    @classmethod
    def patch(cls) -> None: ...

class _BuildMetaBackend:
    def run_setup(self, setup_script: str = ...) -> None: ...
    def get_requires_for_build_wheel(self, config_settings: Incomplete | None = ...): ...
    def get_requires_for_build_sdist(self, config_settings: Incomplete | None = ...): ...
    def prepare_metadata_for_build_wheel(self, metadata_directory, config_settings: Incomplete | None = ...): ...
    def build_wheel(
        self, wheel_directory, config_settings: Incomplete | None = ..., metadata_directory: Incomplete | None = ...
    ): ...
    def build_sdist(self, sdist_directory, config_settings: Incomplete | None = ...): ...
    def build_editable(
        self, wheel_directory, config_settings: Incomplete | None = None, metadata_directory: Incomplete | None = None
    ): ...
    def get_requires_for_build_editable(self, config_settings: Incomplete | None = None) -> list[str]: ...
    def prepare_metadata_for_build_editable(self, metadata_directory, config_settings: Incomplete | None = None) -> str: ...

class _BuildMetaLegacyBackend(_BuildMetaBackend):
    def run_setup(self, setup_script: str = ...) -> None: ...

_BACKEND: _BuildMetaBackend

get_requires_for_build_wheel = _BACKEND.get_requires_for_build_wheel  # noqa: F821
get_requires_for_build_sdist = _BACKEND.get_requires_for_build_sdist  # noqa: F821
prepare_metadata_for_build_wheel = _BACKEND.prepare_metadata_for_build_wheel  # noqa: F821
build_wheel = _BACKEND.build_wheel  # noqa: F821
build_sdist = _BACKEND.build_sdist  # noqa: F821
get_requires_for_build_editable = _BACKEND.get_requires_for_build_editable  # noqa: F821
prepare_metadata_for_build_editable = _BACKEND.prepare_metadata_for_build_editable  # noqa: F821
build_editable = _BACKEND.build_editable  # noqa: F821
__legacy__: Final[_BuildMetaLegacyBackend]
