from _typeshed import Self
from typing import Any, ClassVar, NamedTuple
from typing_extensions import Final

__docformat__: Final[str]
__version__: Final[str]
__version_details__: Final[str]

class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int
    release: bool

class VersionInfo(_VersionInfo):
    def __new__(
        cls: type[Self],
        major: int = ...,
        minor: int = ...,
        micro: int = ...,
        releaselevel: str = ...,
        serial: int = ...,
        release: bool = ...,
    ) -> Self: ...

__version_info__: Final[VersionInfo]

class ApplicationError(Exception): ...
class DataError(ApplicationError): ...

class SettingsSpec:
    settings_spec: ClassVar[tuple[Any, ...]]
    settings_defaults: ClassVar[dict[Any, Any] | None]
    settings_default_overrides: ClassVar[dict[Any, Any] | None]
    relative_path_settings: ClassVar[tuple[Any, ...]]
    config_section: ClassVar[str | None]
    config_section_dependencies: ClassVar[tuple[str, ...] | None]

class TransformSpec:
    def get_transforms(self) -> list[Any]: ...
    default_transforms: ClassVar[tuple[Any, ...]]
    unknown_reference_resolvers: ClassVar[list[Any]]

class Component(SettingsSpec, TransformSpec):
    component_type: ClassVar[str | None]
    supported: ClassVar[tuple[str, ...]]
    def supports(self, format: str) -> bool: ...
