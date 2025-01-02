from typing import IO, Any, ClassVar

class BaseStorage:
    name: str | None
    read_mode: str
    encoding: str | None
    def __init__(self, *, name: str | None = None, read_mode: str = "", encoding: str | None = None) -> None: ...
    def save(self, data: Any) -> None: ...
    def read(self) -> None: ...
    def remove(self) -> None: ...

class TempFolderStorage(BaseStorage):
    def save(self, data: Any) -> None: ...
    def read(self): ...
    def remove(self) -> None: ...
    def get_full_path(self) -> str: ...

class CacheStorage(BaseStorage):
    CACHE_LIFETIME: int
    CACHE_PREFIX: str
    def save(self, data: Any) -> None: ...
    def read(self): ...
    def remove(self) -> None: ...

class MediaStorage(BaseStorage):
    MEDIA_FOLDER: ClassVar[str]
    def save(self, data: IO[Any]) -> None: ...
    def read(self): ...
    def remove(self) -> None: ...
    def get_full_path(self) -> str: ...