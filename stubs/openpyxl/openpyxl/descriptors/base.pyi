from _typeshed import Incomplete, ReadableBuffer, SupportsTrunc
from typing import SupportsFloat, SupportsInt
from typing_extensions import SupportsIndex, TypeAlias

# Helper types for Convertible Descriptors
_IntegerSetter: TypeAlias = str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc  # noqa: Y047
_FloatSetter: TypeAlias = SupportsFloat | SupportsIndex | str | ReadableBuffer  # noqa: Y047
_BoolSetter: TypeAlias = object  # noqa: Y047

class Descriptor:
    name: Incomplete
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Typed(Descriptor):
    expected_type: Incomplete
    allow_none: bool
    nested: bool
    __doc__: Incomplete
    def __init__(self, *args, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Convertible(Typed):
    def __set__(self, instance, value) -> None: ...

class Max(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Min(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class MinMax(Min, Max): ...

class Set(Descriptor):
    __doc__: Incomplete
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class NoneSet(Set):
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Integer(Convertible):
    expected_type: Incomplete

class Float(Convertible):
    expected_type: Incomplete

class Bool(Convertible):
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...

class String(Typed):
    expected_type: Incomplete

class Text(String, Convertible): ...

class ASCII(Typed):
    expected_type: Incomplete

class Tuple(Typed):
    expected_type: Incomplete

class Length(Descriptor):
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Default(Typed):
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __call__(self): ...

class Alias(Descriptor):
    alias: Incomplete
    def __init__(self, alias) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class MatchPattern(Descriptor):
    allow_none: bool
    test_pattern: Incomplete
    def __init__(self, name: Incomplete | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class DateTime(Typed):
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...
