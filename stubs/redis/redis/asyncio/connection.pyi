import asyncio
import enum
import ssl
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Protocol, overload
from typing_extensions import TypeAlias, TypedDict

from redis import RedisError
from redis.asyncio.retry import Retry
from redis.credentials import CredentialProvider
from redis.typing import EncodableT

SYM_STAR: bytes
SYM_DOLLAR: bytes
SYM_CRLF: bytes
SYM_LF: bytes
SYM_EMPTY: bytes

class _Sentinel(enum.Enum):
    sentinel: Any

SENTINEL: object
DefaultParser: type[AsyncBaseParser]

class ConnectCallbackProtocol(Protocol):
    def __call__(self, connection: Connection): ...

class AsyncConnectCallbackProtocol(Protocol):
    async def __call__(self, connection: Connection): ...

ConnectCallbackT: TypeAlias = ConnectCallbackProtocol | AsyncConnectCallbackProtocol

class AbstractConnection:
    db: Incomplete
    client_name: Incomplete
    lib_name: Incomplete
    lib_version: Incomplete
    credential_provider: Incomplete
    password: Incomplete
    username: Incomplete
    socket_timeout: Incomplete
    socket_connect_timeout: Incomplete
    retry_on_timeout: Incomplete
    retry_on_error: Incomplete
    retry: Incomplete
    health_check_interval: Incomplete
    next_health_check: int
    encoder: Incomplete
    redis_connect_func: Incomplete
    protocol: Incomplete
    def __init__(
        self,
        *,
        db: str | int = ...,
        password: str | None = ...,
        socket_timeout: float | None = ...,
        socket_connect_timeout: float | None = ...,
        retry_on_timeout: bool = ...,
        retry_on_error: list[Incomplete] | _Sentinel = ...,
        encoding: str = ...,
        encoding_errors: str = ...,
        decode_responses: bool = ...,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = ...,
        health_check_interval: float = ...,
        client_name: str | None = ...,
        lib_name: str | None = ...,
        lib_version: str | None = ...,
        username: str | None = ...,
        retry: Retry | None = ...,
        redis_connect_func: ConnectCallbackT | None = ...,
        encoder_class: type[Encoder] = ...,
        credential_provider: CredentialProvider | None = ...,
        protocol: int | None = ...,
    ) -> None: ...
    @abstractmethod
    def repr_pieces(self): ...
    @property
    def is_connected(self): ...
    def set_parser(self, parser_class: type[BaseParser]) -> None: ...
    async def connect(self): ...
    async def on_connect(self) -> None: ...
    async def disconnect(self, nowait: bool = ...) -> None: ...
    async def check_health(self) -> None: ...
    async def send_packed_command(self, command: bytes | str | Iterable[bytes], check_health: bool = ...) -> None: ...
    async def send_command(self, *args: Any, **kwargs: Any) -> None: ...
    async def can_read_destructive(self): ...
    async def read_response(
        self,
        disable_decoding: bool = ...,
        timeout: float | None = ...,
        *,
        disconnect_on_error: bool = ...,
        push_request: bool | None = ...,
    ): ...
    def pack_command(self, *args: EncodableT) -> list[bytes]: ...
    def pack_commands(self, commands: Iterable[Iterable[EncodableT]]) -> list[bytes]: ...

class Connection:
    pid: Any
    host: Any
    port: Any
    db: Any
    username: Any
    client_name: Any
    password: Any
    socket_timeout: float | None
    socket_connect_timeout: float | None
    socket_keepalive: Any
    socket_keepalive_options: Any
    socket_type: Any
    retry_on_timeout: Any
    retry_on_error: list[type[RedisError]]
    retry: Retry
    health_check_interval: Any
    next_health_check: int
    ssl_context: Any
    encoder: Any
    redis_connect_func: ConnectCallbackT | None
    def __init__(
        self,
        *,
        host: str = "localhost",
        port: str | int = 6379,
        db: str | int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[int, int | bytes] | None = None,
        socket_type: int = 0,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | _Sentinel = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: ConnectCallbackT | None = None,
        encoder_class: type[Encoder] = ...,
        credential_provider: CredentialProvider | None = None,
    ) -> None: ...
    def repr_pieces(self): ...
    @property
    def is_connected(self): ...
    def set_parser(self, parser_class) -> None: ...
    async def connect(self) -> None: ...
    async def on_connect(self) -> None: ...
    async def disconnect(self, nowait: bool = False) -> None: ...
    async def check_health(self) -> None: ...
    async def send_packed_command(self, command: bytes | str | Iterable[bytes], check_health: bool = True): ...
    async def send_command(self, *args, **kwargs) -> None: ...
    @overload
    async def read_response(self, *, timeout: float, disconnect_on_error: bool = True) -> Incomplete | None: ...
    @overload
    async def read_response(
        self, disable_decoding: bool, timeout: float, *, disconnect_on_error: bool = True
    ) -> Incomplete | None: ...
    @overload
    async def read_response(self, disable_decoding: bool = False, timeout: None = None, *, disconnect_on_error: bool = True): ...
    def pack_command(self, *args: EncodableT) -> list[bytes]: ...
    def pack_commands(self, commands: Iterable[Iterable[EncodableT]]) -> list[bytes]: ...

class SSLConnection(Connection):
    ssl_context: Any
    def __init__(
        self,
        ssl_keyfile: str | None = None,
        ssl_certfile: str | None = None,
        ssl_cert_reqs: str = "required",
        ssl_ca_certs: str | None = None,
        ssl_ca_data: str | None = None,
        ssl_check_hostname: bool = False,
        **kwargs,
    ) -> None: ...
    @property
    def keyfile(self): ...
    @property
    def certfile(self): ...
    @property
    def cert_reqs(self): ...
    @property
    def ca_certs(self): ...
    @property
    def ca_data(self): ...
    @property
    def check_hostname(self): ...

class RedisSSLContext:
    keyfile: Any
    certfile: Any
    cert_reqs: Any
    ca_certs: Any
    ca_data: Any
    check_hostname: Any
    context: Any
    def __init__(
        self,
        keyfile: str | None = None,
        certfile: str | None = None,
        cert_reqs: str | None = None,
        ca_certs: str | None = None,
        ca_data: str | None = None,
        check_hostname: bool = False,
    ) -> None: ...
    def get(self) -> ssl.SSLContext: ...

class UnixDomainSocketConnection(Connection):
    pid: Any
    path: Any
    db: Any
    username: Any
    client_name: Any
    password: Any
    retry_on_timeout: Any
    retry_on_error: list[type[RedisError]]
    retry: Any
    health_check_interval: Any
    next_health_check: int
    redis_connect_func: ConnectCallbackT | None
    encoder: Any
    def __init__(
        self,
        *,
        path: str = "",
        db: str | int = 0,
        username: str | None = None,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | _Sentinel = ...,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: float = 0.0,
        client_name: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: ConnectCallbackT | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> None: ...
    def repr_pieces(self) -> Iterable[tuple[str, str | int]]: ...

FALSE_STRINGS: Any

def to_bool(value) -> bool | None: ...

URL_QUERY_ARGUMENT_PARSERS: Mapping[str, Callable[..., object]]

class ConnectKwargs(TypedDict):
    username: str
    password: str
    connection_class: type[Connection]
    host: str
    port: int
    db: int
    path: str

def parse_url(url: str) -> ConnectKwargs: ...

class ConnectionPool:
    @classmethod
    def from_url(cls, url: str, **kwargs) -> ConnectionPool: ...
    connection_class: Any
    connection_kwargs: Any
    max_connections: Any
    encoder_class: Any
    def __init__(
        self, connection_class: type[Connection] = ..., max_connections: int | None = None, **connection_kwargs
    ) -> None: ...
    pid: Any
    def reset(self) -> None: ...
    async def get_connection(self, command_name, *keys, **options): ...
    def get_encoder(self): ...
    def make_connection(self): ...
    async def release(self, connection: Connection): ...
    async def disconnect(self, inuse_connections: bool = True): ...

class BlockingConnectionPool(ConnectionPool):
    queue_class: Any
    timeout: Any
    def __init__(
        self,
        max_connections: int = 50,
        timeout: int | None = 20,
        connection_class: type[Connection] = ...,
        queue_class: type[asyncio.Queue[Any]] = ...,
        **connection_kwargs,
    ) -> None: ...
    pool: Any
    pid: Any
    def reset(self) -> None: ...
    def make_connection(self): ...
    async def get_connection(self, command_name, *keys, **options): ...
    async def release(self, connection: Connection): ...
    async def disconnect(self, inuse_connections: bool = True): ...
