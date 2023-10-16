from _typeshed import Incomplete
from enum import Enum

class IndexType(Enum):
    HASH: int
    JSON: int

class IndexDefinition:
    args: Incomplete
    def __init__(
        self,
        prefix=...,
        filter: Incomplete | None = ...,
        language_field: Incomplete | None = ...,
        language: Incomplete | None = ...,
        score_field: Incomplete | None = ...,
        score: float = ...,
        payload_field: Incomplete | None = ...,
        index_type: Incomplete | None = ...,
    ) -> None: ...
