from _typeshed import Unused
from collections.abc import Generator, Iterable
from typing import ClassVar, Generic, TypeVar, overload
from typing_extensions import Literal, Self, TypeAlias

from openpyxl.descriptors import Strict
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.utils.indexed_list import IndexedList
from openpyxl.worksheet.cell_range import CellRange
from openpyxl.xml.functions import Element

from .base import _N, _T, Alias, Descriptor, _ConvertibleToInt, _ExpectedTypeParam
from .nested import _HasGet, _HasTextAndAttrib, _T_co

_U = TypeVar("_U", bound=bool)
_SerialisableT = TypeVar("_SerialisableT", bound=Serialisable)
_SequenceParam: TypeAlias = list[_T] | tuple[_T, ...]
_UniqueSequenceParam: TypeAlias = list[_T] | tuple[_T, ...] | set[_T]

class Sequence(Descriptor[_SequenceParam[_T]], Generic[_T, _N, _U]):
    expected_type: type[_T]
    seq_types: ClassVar[tuple[type, ...]]
    idx_base: ClassVar[int]
    unique: _U
    container: ClassVar[type]
    allow_none: _N
    @overload
    def __init__(
        self: Sequence[_T, Literal[True], Literal[True]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        unique: Literal[True],
        allow_none: Literal[True],
    ) -> None: ...
    @overload
    def __init__(
        self: Sequence[_T, Literal[False], Literal[True]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        unique: Literal[True],
        allow_none: Literal[False] = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Sequence[_T, Literal[True], Literal[False]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        unique: Literal[False] = False,
        allow_none: Literal[True],
    ) -> None: ...
    @overload
    def __init__(
        self: Sequence[_T, Literal[False], Literal[False]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        unique: Literal[False] = False,
        allow_none: Literal[False] = False,
    ) -> None: ...
    @overload
    def __get__(
        self: Sequence[_T, Literal[True], Literal[True]], instance: Serialisable | Strict, cls: type | None = None
    ) -> IndexedList[_T | None]: ...
    @overload
    def __get__(
        self: Sequence[_T, Literal[False], Literal[True]], instance: Serialisable | Strict, cls: type | None = None
    ) -> IndexedList[_T]: ...
    @overload
    def __get__(
        self: Sequence[_T, Literal[True], Literal[False]], instance: Serialisable | Strict, cls: type | None = None
    ) -> list[_T | None]: ...
    @overload
    def __get__(
        self: Sequence[_T, Literal[False], Literal[False]], instance: Serialisable | Strict, cls: type | None = None
    ) -> list[_T]: ...
    # NOTE: It is currently impossible to make a generic based on the parameter type of another generic
    # So we implement explicitely the simple convertible types used internally
    #
    # str
    @overload
    def __set__(self: Sequence[str, _N, _U], instance: Serialisable | Strict, value: _SequenceParam[object]) -> None: ...
    # int
    @overload
    def __set__(
        self: Sequence[int, Literal[True], _U], instance: Serialisable | Strict, value: _SequenceParam[_ConvertibleToInt | None]
    ) -> None: ...
    @overload
    def __set__(
        self: Sequence[int, Literal[False], _U], instance: Serialisable | Strict, value: _SequenceParam[_ConvertibleToInt]
    ) -> None: ...
    # Most Serialisable subclasses have an optional first parameter to __init__, so this results in less false-positives
    @overload
    def __set__(
        self: Sequence[_SerialisableT, _N, _U], instance: Serialisable | Strict, value: _SequenceParam[_SerialisableT | None]
    ) -> None: ...
    # everything else
    @overload
    def __set__(
        self: Sequence[_T, Literal[True], _U], instance: Serialisable | Strict, value: _SequenceParam[_T | None]
    ) -> None: ...
    @overload
    def __set__(self: Sequence[_T, Literal[False], _U], instance: Serialisable | Strict, value: _SequenceParam[_T]) -> None: ...
    def to_tree(self, tagname: str, obj: Iterable[object], namespace: str | None = None) -> Generator[Element, None, None]: ...

class UniqueSequence(Sequence[_T, _N, _U]):
    seq_types: ClassVar[tuple[type, ...]]
    container: ClassVar[type]
    @overload  # type: ignore[override]
    def __get__(
        self: UniqueSequence[_T, Literal[True], Literal[True]], instance: Serialisable | Strict, cls: type | None = None
    ) -> IndexedList[_T | None]: ...
    @overload
    def __get__(
        self: UniqueSequence[_T, Literal[False], Literal[True]], instance: Serialisable | Strict, cls: type | None = None
    ) -> IndexedList[_T]: ...
    @overload
    def __get__(
        self: UniqueSequence[_T, Literal[True], Literal[False]], instance: Serialisable | Strict, cls: type | None = None
    ) -> set[_T | None]: ...
    @overload
    def __get__(
        self: UniqueSequence[_T, Literal[False], Literal[False]], instance: Serialisable | Strict, cls: type | None = None
    ) -> set[_T]: ...
    # NOTE: It is currently impossible to make a generic based on the parameter type of another generic
    # So we implement explicitely the types used internally
    #
    # CellRange
    @overload
    def __set__(
        self: UniqueSequence[CellRange, _N, _U],
        instance: Serialisable | Strict,
        value: _UniqueSequenceParam[CellRange | str | None],
    ) -> None: ...
    # str
    @overload
    def __set__(
        self: UniqueSequence[str, _N, _U], instance: Serialisable | Strict, value: _UniqueSequenceParam[object]
    ) -> None: ...
    # int
    @overload
    def __set__(
        self: UniqueSequence[int, Literal[True], _U],
        instance: Serialisable | Strict,
        value: _UniqueSequenceParam[_ConvertibleToInt | None],
    ) -> None: ...
    @overload
    def __set__(
        self: UniqueSequence[int, Literal[False], _U],
        instance: Serialisable | Strict,
        value: _UniqueSequenceParam[_ConvertibleToInt],
    ) -> None: ...
    # everything else
    @overload
    def __set__(
        self: UniqueSequence[_T, Literal[True], _U], instance: Serialisable | Strict, value: _UniqueSequenceParam[_T | None]
    ) -> None: ...
    @overload
    def __set__(
        self: UniqueSequence[_T, Literal[False], _U], instance: Serialisable | Strict, value: _UniqueSequenceParam[_T]
    ) -> None: ...

class ValueSequence(Sequence[_T, _N, _U]):
    attribute: ClassVar[str]
    def to_tree(self, tagname: str, obj, namespace: str | None = None) -> Generator[Element, None, None]: ...
    def from_tree(self, node: _HasGet[_T_co]) -> _T_co: ...

class NestedSequence(Sequence[_SerialisableT, _N, _U]):
    count: bool
    expected_type: type[_SerialisableT]
    def to_tree(self, tagname: str, obj, namespace: str | None = None) -> Element: ...  # type: ignore[override]
    def from_tree(self, node: _HasTextAndAttrib) -> list[_SerialisableT]: ...

# Literal[False] : Don't automatically add "None" or "IndexedList" to possible __get__ return type
class MultiSequence(Sequence[_T, Literal[False], Literal[False]]):
    def __set__(self: MultiSequence[_T], instance: Serialisable | Strict, value: _SequenceParam[_T]) -> None: ...
    def to_tree(self, tagname: str, obj, namespace: str | None = None) -> Generator[Element, None, None]: ...

class MultiSequencePart(Alias, Generic[_T]):
    expected_type: type[_T]
    store: str
    def __init__(self, expected_type: type[_T], store: str) -> None: ...
    # NOTE: It is currently impossible to make a generic based on the parameter type of another generic
    # Since MultiSequencePart is only used with Serialisable subclasses internally,
    # we pretend the setter value is not convertible
    def __set__(self, instance: Serialisable | Strict, value: _T) -> None: ...
    def __get__(self, instance: Unused, cls: Unused) -> Self: ...
