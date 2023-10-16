from _typeshed import Incomplete
from typing import Any

from ...client import Pipeline as ClientPipeline, _StrType
from ...cluster import ClusterPipeline as ClusterClusterPipeline
from .commands import JSONCommands

class JSON(JSONCommands):
    MODULE_CALLBACKS: dict[str, Any]
    client: Any
    execute_command: Any
    MODULE_VERSION: Incomplete | None
    def __init__(self, client, version: Incomplete | None = None, decoder=..., encoder=...) -> None: ...
    def pipeline(self, transaction: bool = True, shard_hint: Incomplete | None = None) -> Pipeline[Incomplete]: ...

class ClusterPipeline(JSONCommands, ClusterClusterPipeline[_StrType]): ...  # type: ignore[misc]  # Incompatible base class
class Pipeline(JSONCommands, ClientPipeline[_StrType]): ...  # type: ignore[misc]  # Incompatible base class
