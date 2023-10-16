from _typeshed import Incomplete

from ...asyncio.client import Pipeline as AsyncioPipeline
from ...client import Pipeline as RedisClientPipeline, _StrType
from .commands import AsyncSearchCommands, SearchCommands

class Search(SearchCommands):
    class BatchIndexer:
        client: Incomplete
        execute_command: Incomplete
        total: int
        chunk_size: Incomplete
        current_chunk: int
        def __init__(self, client, chunk_size: int = 1000) -> None: ...
        def __del__(self) -> None: ...
        def add_document(
            self,
            doc_id,
            nosave: bool = False,
            score: float = 1.0,
            payload: Incomplete | None = None,
            replace: bool = False,
            partial: bool = False,
            no_create: bool = False,
            **fields,
        ): ...
        def add_document_hash(self, doc_id, score: float = 1.0, replace: bool = False): ...
        def commit(self): ...
    client: Incomplete
    index_name: Incomplete
    execute_command: Incomplete
    def __init__(self, client, index_name: str = "idx") -> None: ...
    def pipeline(self, transaction: bool = ..., shard_hint: Incomplete | None = ...): ...

class AsyncSearch(Search, AsyncSearchCommands):
    class BatchIndexer(Search.BatchIndexer):
        async def add_document(
            self,
            doc_id,
            nosave: bool = ...,
            score: float = ...,
            payload: Incomplete | None = ...,
            replace: bool = ...,
            partial: bool = ...,
            no_create: bool = ...,
            **fields,
        ) -> None: ...
        current_chunk: int
        async def commit(self) -> None: ...

    def pipeline(self, transaction: bool = ..., shard_hint: Incomplete | None = ...): ...

class Pipeline(SearchCommands, RedisClientPipeline[_StrType]): ...  # type: ignore[misc]  # Incompatible base class
class AsyncPipeline(AsyncSearchCommands, AsyncioPipeline[_StrType], Pipeline[_StrType]): ...  # type: ignore[misc]  # Incompatible base class  # pyright: ignore  # MRO
