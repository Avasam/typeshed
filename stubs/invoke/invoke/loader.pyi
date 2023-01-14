from types import ModuleType
from typing import IO, Any

from . import Config

class Loader:
    config: Config
    def __init__(self, config: Config | None = ...) -> None: ...
    def find(self, name: str) -> tuple[str, IO, str, tuple[str, str, int]]: ...
    def load(self, name: str | None = ...) -> tuple[ModuleType, str]: ...

class FilesystemLoader(Loader):
    def __init__(self, start: str | None = ..., **kwargs: Any) -> None: ...
    @property
    def start(self) -> str: ...
