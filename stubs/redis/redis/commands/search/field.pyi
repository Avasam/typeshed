from _typeshed import Incomplete

from redis import DataError as DataError

class Field:
    NUMERIC: str
    TEXT: str
    WEIGHT: str
    GEO: str
    TAG: str
    VECTOR: str
    SORTABLE: str
    NOINDEX: str
    AS: str
    name: Incomplete
    args: Incomplete
    args_suffix: Incomplete
    as_name: Incomplete
    def __init__(
        self, name: str, args: list[str] = ..., sortable: bool = ..., no_index: bool = ..., as_name: str = ...
    ) -> None: ...
    def append_arg(self, value) -> None: ...
    def redis_args(self): ...

class TextField(Field):
    NOSTEM: str
    PHONETIC: str
    def __init__(
        self,
        name: str,
        weight: float = ...,
        no_stem: bool = ...,
        phonetic_matcher: str = ...,
        withsuffixtrie: bool = ...,
        **kwargs,
    ) -> None: ...

class NumericField(Field):
    def __init__(self, name: str, **kwargs) -> None: ...

class GeoField(Field):
    def __init__(self, name: str, **kwargs) -> None: ...

class TagField(Field):
    SEPARATOR: str
    CASESENSITIVE: str
    def __init__(
        self, name: str, separator: str = ..., case_sensitive: bool = ..., withsuffixtrie: bool = ..., **kwargs
    ) -> None: ...

class VectorField(Field):
    def __init__(self, name: str, algorithm: str, attributes: dict[Incomplete, Incomplete], **kwargs) -> None: ...
