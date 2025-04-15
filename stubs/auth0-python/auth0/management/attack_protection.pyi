from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class AttackProtection:
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
    def get_breached_password_detection(self) -> dict[str, Incomplete]: ...
    def update_breached_password_detection(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_brute_force_protection(self) -> dict[str, Incomplete]: ...
    def update_brute_force_protection(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_suspicious_ip_throttling(self) -> dict[str, Incomplete]: ...
    def update_suspicious_ip_throttling(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
