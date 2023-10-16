from collections.abc import Iterable, Mapping
from datetime import datetime, timedelta
from typing import Protocol, TypeVar
from typing_extensions import TypeAlias

# The following type aliases exist at runtime.
Number: TypeAlias = int | float
EncodedT: TypeAlias = bytes | memoryview
DecodedT: TypeAlias = str | int | float
EncodableT: TypeAlias = EncodedT | DecodedT
AbsExpiryT: TypeAlias = int | datetime
ExpiryT: TypeAlias = float | timedelta
ZScoreBoundT: TypeAlias = float | str
BitfieldOffsetT: TypeAlias = int | str
_StringLikeT: TypeAlias = bytes | str | memoryview  # noqa: Y043
KeyT: TypeAlias = _StringLikeT
PatternT: TypeAlias = _StringLikeT
FieldT: TypeAlias = EncodableT
KeysT: TypeAlias = KeyT | Iterable[KeyT]
ChannelT: TypeAlias = _StringLikeT
GroupT: TypeAlias = _StringLikeT
ConsumerT: TypeAlias = _StringLikeT
StreamIdT: TypeAlias = int | _StringLikeT
ScriptTextT: TypeAlias = _StringLikeT
TimeoutSecT: TypeAlias = int | float | _StringLikeT
AnyKeyT = TypeVar("AnyKeyT", bytes, str, memoryview)  # noqa: Y001
AnyFieldT = TypeVar("AnyFieldT", bytes, str, memoryview)  # noqa: Y001
AnyChannelT = TypeVar("AnyChannelT", bytes, str, memoryview)  # noqa: Y001
ExceptionMappingT: TypeAlias = Mapping[str, type[Exception] | Mapping[str, type[Exception]]]

class CommandsProtocol(Protocol):
    # Not enforcing this as part of the protocol is the least disruptive short-term to fix metaclass issues
    # See: https://github.com/python/typeshed/issues/9127
    # and https://github.com/redis/redis-py/issues/2730
    # connection_pool: AsyncConnectionPool | ConnectionPool
    def execute_command(self, *args, **options): ...

class ClusterCommandsProtocol(CommandsProtocol, Protocol):
    # Not enforcing this as part of the protocol is the least disruptive short-term to fix metaclass issues
    # See: https://github.com/python/typeshed/issues/9127
    # and https://github.com/redis/redis-py/issues/2730
    # encoder: Encoder
    # def execute_command(self, *args, **options) -> Any | Awaitable[Incomplete]: ...
    ...
