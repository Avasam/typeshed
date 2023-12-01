from _typeshed import Unused
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from email.contentmanager import ContentManager
from email.errors import MessageDefect
from email.header import Header
from email.headerregistry import BaseHeader
from email.message import Message
from typing import Any, Protocol, TypeVar, overload
from typing_extensions import Self

__all__ = ["Compat32", "compat32", "Policy", "EmailPolicy", "default", "strict", "SMTP", "HTTP"]

class _HasName(Protocol):
    name: str

_HasNameT = TypeVar("_HasNameT", bound=_HasName)
_HeaderT = TypeVar("_HeaderT", bound=Header)
_StrBaseHeader = TypeVar("_StrBaseHeader", bound=str)  # BaseHeader matches this bound

class Policy(metaclass=ABCMeta):
    max_line_length: int | None
    linesep: str
    cte_type: str
    raise_on_defect: bool
    mangle_from_: bool
    message_factory: Callable[[Policy], Message] | None
    def __init__(
        self,
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: Callable[[Policy], Message] | None = ...,
    ) -> None: ...
    def clone(self, **kw: Any) -> Self: ...
    def handle_defect(self, obj: Message, defect: MessageDefect) -> None: ...
    def register_defect(self, obj: Message, defect: MessageDefect) -> None: ...
    def header_max_count(self, name: str) -> int | None: ...
    @abstractmethod
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    @abstractmethod
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]: ...
    @abstractmethod
    def header_fetch_parse(self, name: str, value: str) -> str | Header: ...
    @abstractmethod
    def fold(self, name: str, value: str) -> str: ...
    @abstractmethod
    def fold_binary(self, name: str, value: str) -> bytes: ...

class Compat32(Policy):
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]: ...
    @overload
    def header_fetch_parse(self, name: Unused, value: _HeaderT) -> _HeaderT: ...
    @overload
    def header_fetch_parse(self, name: str, value: _StrBaseHeader) -> _StrBaseHeader | Header: ...
    def fold(self, name: str, value: str) -> str: ...
    def fold_binary(self, name: str, value: str) -> bytes: ...

compat32: Compat32

class EmailPolicy(Policy):
    utf8: bool
    refold_source: str
    header_factory: Callable[[str, Any], Any]
    content_manager: ContentManager
    def __init__(
        self,
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: Callable[[Policy], Message] | None = ...,
        utf8: bool = ...,
        refold_source: str = ...,
        header_factory: Callable[[str, str], str] = ...,
        content_manager: ContentManager = ...,
    ) -> None: ...
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    def header_store_parse(self, name: str, value: Any) -> tuple[str, Any]: ...
    @overload
    def header_fetch_parse(self, name: Unused, value: _HasNameT) -> _HasNameT: ...
    @overload
    def header_fetch_parse(self, name: str, value: str) -> BaseHeader: ...
    def fold(self, name: str, value: str) -> Any: ...
    def fold_binary(self, name: str, value: str) -> bytes: ...

default: EmailPolicy
SMTP: EmailPolicy
SMTPUTF8: EmailPolicy
HTTP: EmailPolicy
strict: EmailPolicy
