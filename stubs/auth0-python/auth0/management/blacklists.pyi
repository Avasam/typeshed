from _typeshed import Incomplete

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Blacklists:
    url: Incomplete
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
    def get(self, aud: str | None = None) -> list[dict[str, str]]: ...
    def create(self, jti: str, aud: str | None = None) -> dict[str, str]: ...
