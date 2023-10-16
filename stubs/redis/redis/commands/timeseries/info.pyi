from _typeshed import Incomplete
from typing import Any

class TSInfo:
    rules: list[Any]
    labels: list[Any]
    sourceKey: Incomplete | None
    chunk_count: Incomplete | None
    memory_usage: Incomplete | None
    total_samples: Incomplete | None
    retention_msecs: Incomplete | None
    last_time_stamp: Incomplete | None
    first_time_stamp: Incomplete | None
    max_samples_per_chunk: Incomplete | None
    chunk_size: Incomplete | None
    duplicate_policy: Incomplete | None
    source_key: Incomplete
    last_timestamp: Incomplete
    first_timestamp: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...
