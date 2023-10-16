from _typeshed import Incomplete, Unused
from abc import abstractmethod
from collections.abc import Callable, Iterable, Mapping
from queue import Queue
from typing import Any
from typing_extensions import Self, TypeAlias

from ._parsers.base import BaseParser
from ._parsers.encoders import Encoder
from .credentials import CredentialProvider
from .retry import Retry

# Options as passed to Pool.get_connection().
_ConnectionPoolOptions: TypeAlias = Any
_ConnectFunc: TypeAlias = Callable[[Connection], object]

SYM_STAR: bytes
SYM_DOLLAR: bytes
SYM_CRLF: bytes
SYM_EMPTY: bytes
DEFAULT_RESP_VERSION: int
SENTINEL: object
DefaultParser: type[BaseParser]  # _HiredisParser or _RESP2Parser

FALSE_STRINGS: tuple[str, ...]
URL_QUERY_ARGUMENT_PARSERS: dict[str, Callable[[Any], Any]]

class HiredisRespSerializer:
    def pack(self, *args: list[Incomplete]): ...

class PythonRespSerializer:
    encode: Incomplete
    def __init__(self, buffer_cutoff, encode) -> None: ...
    def pack(self, *args): ...

class AbstractConnection:
    pid: int
    db: int
    client_name: str | None
    credential_provider: CredentialProvider | None
    password: str | None
    username: str | None
    socket_timeout: float | None
    socket_connect_timeout: float | None
    retry_on_timeout: bool
    retry_on_error: list[type[Exception]]
    retry: Retry
    health_check_interval: int
    next_health_check: int
    redis_connect_func: _ConnectFunc | None
    encoder: Encoder

    def __init__(
        self,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...
    @abstractmethod
    def repr_pieces(self) -> list[tuple[str, Any]]: ...
    def set_parser(self, parser_class: type[BaseParser]) -> None: ...
    def connect(self) -> None: ...
    def on_connect(self) -> None: ...
    def disconnect(self, *args: Unused) -> None: ...  # 'args' added in redis 4.1.2
    def check_health(self) -> None: ...
    def send_packed_command(self, command: str | Iterable[str], check_health: bool = True) -> None: ...
    def send_command(self, *args, **kwargs) -> None: ...
    def can_read(self, timeout: float | None = 0) -> bool: ...
    def read_response(
        self, disable_decoding: bool = False, *, disconnect_on_error: bool = True
    ) -> Any: ...  # AnyOf[str | bytes | list[str | bytes]]
    def pack_command(self, *args) -> list[bytes]: ...
    def pack_commands(self, commands: Iterable[Iterable[Incomplete]]) -> list[bytes]: ...

class Connection(AbstractConnection):
    host: str
    port: int
    socket_keepalive: bool
    socket_keepalive_options: Mapping[str, int | str]
    socket_type: int
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        socket_type: int = 0,
        *,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...
    def repr_pieces(self) -> list[tuple[str, Any]]: ...

class SSLConnection(Connection):
    keyfile: Any
    certfile: Any
    cert_reqs: Any
    ca_certs: Any
    ca_path: Incomplete | None
    check_hostname: bool
    certificate_password: Incomplete | None
    ssl_validate_ocsp: bool
    ssl_validate_ocsp_stapled: bool  # added in 4.1.1
    ssl_ocsp_context: Incomplete | None  # added in 4.1.1
    ssl_ocsp_expected_cert: Incomplete | None  # added in 4.1.1
    def __init__(
        self,
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_cert_reqs="required",
        ssl_ca_certs=None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = False,
        ssl_ca_path: Incomplete | None = None,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        *,
        host: str = "localhost",
        port: int = 6379,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        socket_type: int = 0,
        db: int = 0,
        password: str | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...

class UnixDomainSocketConnection(AbstractConnection):
    path: str
    def __init__(
        self,
        path: str = "",
        *,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...
    def repr_pieces(self) -> list[tuple[str, Any]]: ...

# TODO: make generic on `connection_class`
class ConnectionPool:
    connection_class: type[Connection]
    connection_kwargs: dict[str, Any]
    max_connections: int
    pid: int
    @classmethod
    def from_url(cls, url: str, *, db: int = ..., decode_components: bool = ..., **kwargs) -> Self: ...
    def __init__(
        self, connection_class: type[AbstractConnection] = ..., max_connections: int | None = None, **connection_kwargs
    ) -> None: ...
    def reset(self) -> None: ...
    def get_connection(self, command_name: Unused, *keys, **options: _ConnectionPoolOptions) -> Connection: ...
    def make_connection(self) -> Connection: ...
    def release(self, connection: Connection) -> None: ...
    def disconnect(self, inuse_connections: bool = True) -> None: ...
    def get_encoder(self) -> Encoder: ...
    def owns_connection(self, connection: Connection) -> bool: ...

class BlockingConnectionPool(ConnectionPool):
    queue_class: type[Queue[Any]]
    timeout: float
    pool: Queue[Connection | None]  # might not be defined
    def __init__(
        self,
        max_connections: int = 50,
        timeout: float = 20,
        connection_class: type[Connection] = ...,
        queue_class: type[Queue[Any]] = ...,
        **connection_kwargs,
    ) -> None: ...
    def disconnect(self) -> None: ...  # type: ignore[override]

def to_bool(value: object) -> bool: ...
def parse_url(url: str) -> dict[str, Any]: ...
