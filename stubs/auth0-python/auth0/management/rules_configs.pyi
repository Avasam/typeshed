from _typeshed import Incomplete

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class RulesConfigs:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def all(self) -> list[dict[str, Incomplete]]: ...
    def unset(self, key: str): ...
    def set(self, key: str, value: str) -> dict[str, Incomplete]: ...
