from _typeshed import Incomplete

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Actions:
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
    def get_actions(
        self,
        trigger_id: str | None = None,
        action_name: str | None = None,
        deployed: bool | None = None,
        installed: bool = False,
        page: int | None = None,
        per_page: int | None = None,
    ): ...
    def create_action(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def update_action(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_action(self, id: str) -> dict[str, Incomplete]: ...
    def delete_action(self, id: str, force: bool = False): ...
    def get_triggers(self) -> dict[str, Incomplete]: ...
    def get_execution(self, id: str) -> dict[str, Incomplete]: ...
    def get_action_versions(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Incomplete]: ...
    def get_trigger_bindings(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Incomplete]: ...
    def get_action_version(self, action_id: str, version_id: str) -> dict[str, Incomplete]: ...
    def deploy_action(self, id: str) -> dict[str, Incomplete]: ...
    def rollback_action_version(self, action_id: str, version_id: str) -> dict[str, Incomplete]: ...
    def update_trigger_bindings(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
