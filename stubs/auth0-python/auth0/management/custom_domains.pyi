from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class CustomDomains:
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
    def get(self, id: str) -> dict[str, Incomplete]: ...
    def delete(self, id: str): ...
    def create_new(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def verify(self, id: str) -> dict[str, Incomplete]: ...
