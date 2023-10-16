from typing import ClassVar

from .aggregation import Asc as Asc, Desc as Desc, Reducer as Reducer, SortDirection as SortDirection

class FieldOnlyReducer(Reducer):
    def __init__(self, field: str) -> None: ...

class count(Reducer):
    NAME: ClassVar[str]
    def __init__(self) -> None: ...

class sum(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class min(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class max(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class avg(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class tolist(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class count_distinct(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class count_distinctish(FieldOnlyReducer):
    NAME: ClassVar[str]

class quantile(Reducer):
    NAME: ClassVar[str]
    def __init__(self, field: str, pct: float) -> None: ...

class stddev(FieldOnlyReducer):
    NAME: ClassVar[str]
    def __init__(self, field: str) -> None: ...

class first_value(Reducer):
    NAME: ClassVar[str]
    def __init__(self, field: str, *byfields: Asc | Desc) -> None: ...

class random_sample(Reducer):
    NAME: ClassVar[str]
    def __init__(self, field: str, size: int) -> None: ...
