from _typeshed import Incomplete
from collections.abc import AsyncIterator, Iterable, Mapping, Sequence
from typing import Any, overload

from redis.asyncio.connection import Connection, ConnectionPool, SSLConnection
from redis.commands import AsyncSentinelCommands
from redis.exceptions import ConnectionError
from redis.typing import EncodableT

from .client import Redis

class MasterNotFoundError(ConnectionError): ...
class SlaveNotFoundError(ConnectionError): ...

class SentinelManagedConnection(Connection):
    connection_pool: Any
    def __init__(self, **kwargs) -> None: ...
    async def connect_to(self, address) -> None: ...
    async def connect(self): ...
    @overload  # type: ignore[override]
    async def read_response(self, *, timeout: float, disconnect_on_error: bool = True) -> Incomplete | None: ...
    @overload
    async def read_response(
        self, disable_decoding: bool, timeout: float, *, disconnect_on_error: bool = True
    ) -> Incomplete | None: ...
    @overload
    async def read_response(self, disable_decoding: bool = False, timeout: None = None, *, disconnect_on_error: bool = True): ...

class SentinelManagedSSLConnection(SentinelManagedConnection, SSLConnection): ...

class SentinelConnectionPool(ConnectionPool):
    is_master: Any
    check_connection: Any
    service_name: Any
    sentinel_manager: Any
    master_address: Any
    slave_rr_counter: Any
    def __init__(self, service_name, sentinel_manager, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def owns_connection(self, connection: Connection): ...
    async def get_master_address(self): ...
    async def rotate_slaves(self) -> AsyncIterator[Any]: ...

class Sentinel(AsyncSentinelCommands):
    sentinel_kwargs: Any
    sentinels: Any
    min_other_sentinels: Any
    connection_kwargs: Any
    def __init__(
        self, sentinels, min_other_sentinels: int = 0, sentinel_kwargs: Incomplete | None = None, **connection_kwargs
    ) -> None: ...
    async def execute_command(self, *args, **kwargs): ...
    def check_master_state(self, state: dict[Any, Any], service_name: str) -> bool: ...
    async def discover_master(self, service_name: str): ...
    def filter_slaves(self, slaves: Iterable[Mapping[Any, Any]]) -> Sequence[tuple[EncodableT, EncodableT]]: ...
    async def discover_slaves(self, service_name: str) -> Sequence[tuple[EncodableT, EncodableT]]: ...
    def master_for(
        self,
        service_name: str,
        redis_class: type[Redis[Any]] = ...,
        connection_pool_class: type[SentinelConnectionPool] = ...,
        **kwargs,
    ): ...
    def slave_for(
        self,
        service_name: str,
        redis_class: type[Redis[Any]] = ...,
        connection_pool_class: type[SentinelConnectionPool] = ...,
        **kwargs,
    ): ...
