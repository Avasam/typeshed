from _typeshed import Incomplete
from keyword import iskeyword as iskeyword

error: str

class NotSupportedException(Exception): ...

DropIndirection: str
NoTranslateTypes: Incomplete
NoTranslateMap: Incomplete

class MapEntry:
    dispid: Incomplete
    desc: Incomplete
    names: Incomplete
    doc: Incomplete
    resultCLSID: Incomplete
    resultDocumentation: Incomplete
    wasProperty: int
    hidden: Incomplete
    def __init__(
        self,
        desc_or_id,
        names: Incomplete | None = ...,
        doc: Incomplete | None = ...,
        resultCLSID=...,
        resultDoc: Incomplete | None = ...,
        hidden: int = ...,
    ) -> None: ...
    def GetResultCLSID(self): ...
    def GetResultCLSIDStr(self): ...
    def GetResultName(self): ...

class OleItem:
    typename: str
    doc: Incomplete
    python_name: Incomplete
    bWritten: int
    bIsDispatch: int
    bIsSink: int
    clsid: Incomplete
    co_class: Incomplete
    def __init__(self, doc: Incomplete | None = ...) -> None: ...

class DispatchItem(OleItem):
    typename: str
    propMap: Incomplete
    propMapGet: Incomplete
    propMapPut: Incomplete
    mapFuncs: Incomplete
    defaultDispatchName: Incomplete
    hidden: int
    def __init__(
        self, typeinfo: Incomplete | None = ..., attr: Incomplete | None = ..., doc: Incomplete | None = ..., bForUser: int = ...
    ) -> None: ...
    clsid: Incomplete
    bIsDispatch: Incomplete
    def Build(self, typeinfo, attr, bForUser: int = ...) -> None: ...
    def CountInOutOptArgs(self, argTuple): ...
    def MakeFuncMethod(self, entry, name, bMakeClass: int = ...): ...
    def MakeDispatchFuncMethod(self, entry, name, bMakeClass: int = ...): ...
    def MakeVarArgsFuncMethod(self, entry, name, bMakeClass: int = ...): ...

class VTableItem(DispatchItem):
    vtableFuncs: Incomplete
    def Build(self, typeinfo, attr, bForUser: int = ...): ...

class LazyDispatchItem(DispatchItem):
    typename: str
    clsid: Incomplete
    def __init__(self, attr, doc) -> None: ...

typeSubstMap: Incomplete
valid_identifier_chars: Incomplete

def demunge_leading_underscores(className): ...
def MakePublicAttributeName(className, is_global: bool = ...): ...
def MakeDefaultArgRepr(defArgVal): ...
def BuildCallList(fdesc, names, defNamedOptArg, defNamedNotOptArg, defUnnamedArg, defOutArg, is_comment: bool = ...): ...
