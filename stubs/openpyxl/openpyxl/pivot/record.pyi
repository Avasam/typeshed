from _typeshed import Incomplete, Unused
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.sequence import MultiSequence, MultiSequencePart, _SequenceParam
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.pivot.fields import Boolean, DateTimeField, Error, Index, Missing, Number, Text

_RecordFields: TypeAlias = Missing | Number | Boolean | Error | Text | DateTimeField | Index

class Record(Serialisable):
    tagname: ClassVar[str]
    _fields: MultiSequence[_RecordFields]
    m: MultiSequencePart[Missing]
    n: MultiSequencePart[Number]
    b: MultiSequencePart[Boolean]
    e: MultiSequencePart[Error]
    s: MultiSequencePart[Text]
    d: MultiSequencePart[DateTimeField]
    x: MultiSequencePart[Index]
    def __init__(
        self,
        _fields: _SequenceParam[_RecordFields] = (),
        m: Unused = None,
        n: Unused = None,
        b: Unused = None,
        e: Unused = None,
        s: Unused = None,
        d: Unused = None,
        x: Unused = None,
    ) -> None: ...

class RecordList(Serialisable):
    mime_type: str
    rel_type: str
    tagname: ClassVar[str]
    r: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    __attrs__: ClassVar[tuple[str, ...]]
    def __init__(self, count: Unused = None, r=(), extLst: ExtensionList | None = None) -> None: ...
    @property
    def count(self): ...
    def to_tree(self): ...
    @property
    def path(self): ...
