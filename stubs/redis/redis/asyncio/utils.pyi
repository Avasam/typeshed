from types import TracebackType
from typing import Any, Generic

from ..client import _StrType
from .client import Pipeline, Redis

def from_url(url: str, **kwargs) -> Redis[Any]: ...

class pipeline(Generic[_StrType]):
    p: Pipeline[_StrType]
    def __init__(self, redis_obj: Redis[_StrType]) -> None: ...
    async def __aenter__(self) -> Pipeline[_StrType]: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
