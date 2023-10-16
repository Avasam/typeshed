from _typeshed import Incomplete
from typing import Any

class BFInfo:
    capacity: Any
    size: Any
    filterNum: Any
    insertedNum: Any
    expansionRate: Any
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...

class CFInfo:
    size: Any
    bucketNum: Any
    filterNum: Any
    insertedNum: Any
    deletedNum: Any
    bucketSize: Any
    expansionRate: Any
    maxIteration: Any
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...

class CMSInfo:
    width: Any
    depth: Any
    count: Any
    def __init__(self, args) -> None: ...
    def __getitem__(self, item): ...

class TopKInfo:
    k: Any
    width: Any
    depth: Any
    decay: Any
    def __init__(self, args) -> None: ...
    def __getitem__(self, item): ...

class TDigestInfo:
    compression: Any
    capacity: Any
    mergedNodes: Any
    unmergedNodes: Any
    mergedWeight: Any
    unmergedWeight: Any
    totalCompressions: Any
    memory_usage: Incomplete
    def __init__(self, args) -> None: ...
    def get(self, item): ...
    def __getitem__(self, item): ...
