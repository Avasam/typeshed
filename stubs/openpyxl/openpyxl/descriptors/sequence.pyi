from _typeshed import Incomplete
from collections.abc import Generator
from typing import Generic, TypeVar
from typing_extensions import TypeAlias

from .base import Alias, Descriptor

_T = TypeVar("_T")
_TType = TypeVar("_TType", bound=type)
# Acceptable types for openpyxl.descriptors.Sequence
_Sequence: TypeAlias = tuple[_T, ...] | list[_T]  # noqa: Y047

class Sequence(Descriptor):
    expected_type: type
    seq_types: Incomplete
    idx_base: int
    unique: bool
    def __set__(self, instance, seq) -> None: ...
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...

class ValueSequence(Sequence):
    attribute: str
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def from_tree(self, node): ...

class NestedSequence(Sequence):
    count: bool
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None): ...
    def from_tree(self, node): ...

class MultiSequence(Sequence):
    def __set__(self, instance, seq) -> None: ...
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...

class MultiSequencePart(Alias, Generic[_TType]):
    expected_type: _TType
    store: Incomplete
    def __init__(self, expected_type: _TType, store) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...
