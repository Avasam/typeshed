from typing import ClassVar, final, overload
from typing_extensions import TypeAlias, deprecated

import _win32typing
from win32.lib.pywintypes import IIDType, com_error

error: TypeAlias = com_error  # noqa: Y042

def PSGetItemPropertyHandler(
    Item: _win32typing.PyIShellItem, riid: IIDType, ReadWrite: int, /
) -> _win32typing.PyIPropertyStore: ...
def PSGetPropertyDescription(Key: _win32typing.PyPROPERTYKEY, riid: IIDType, /) -> _win32typing.PyIPropertyDescription: ...
def PSGetPropertySystem(riid: IIDType, /) -> _win32typing.PyIPropertySystem: ...
def PSGetNameFromPropertyKey(Key: _win32typing.PyPROPERTYKEY, /) -> str: ...
def PSGetPropertyKeyFromName(Name, /) -> _win32typing.PyPROPERTYKEY: ...
def PSRegisterPropertySchema(filename, /) -> None: ...
def PSUnregisterPropertySchema(filename, /) -> None: ...
def SHGetPropertyStoreFromParsingName(
    Path: str, Flags, riid: IIDType, BindCtx: _win32typing.PyIBindCtx | None = ..., /
) -> _win32typing.PyIPropertyStore: ...
def StgSerializePropVariant(propvar: PROPVARIANTType, /): ...
def StgDeserializePropVariant(prop, /) -> PROPVARIANTType: ...
def PSCreateMemoryPropertyStore(riid: IIDType, /) -> _win32typing.PyIPropertyStore: ...
def PSCreatePropertyStoreFromPropertySetStorage(
    pss: _win32typing.PyIPropertySetStorage, Mode, riid: IIDType, /
) -> _win32typing.PyIPropertyStore: ...
def PSLookupPropertyHandlerCLSID(FilePath, /) -> IIDType: ...
def SHGetPropertyStoreForWindow(hwnd: int, riid: IIDType, /) -> _win32typing.PyIPropertyStore: ...
def PSGetPropertyFromPropertyStorage(ps, key: _win32typing.PyPROPERTYKEY, /) -> PROPVARIANTType: ...
def PSGetNamedPropertyFromPropertyStorage(ps, name, /) -> PROPVARIANTType: ...
def PSCreateSimplePropertyChange(
    flags, key: _win32typing.PyPROPERTYKEY, val: PROPVARIANTType, riid: IIDType, /
) -> _win32typing.PyIPropertyChange: ...
def PSCreatePropertyChangeArray() -> _win32typing.PyIPropertyChangeArray: ...
def SHSetDefaultProperties(
    hwnd: int,
    Item: _win32typing.PyIShellItem,
    FileOpFlags: int = ...,
    Sink: _win32typing.PyGFileOperationProgressSink | None = ...,
    /,
) -> None: ...

IID_IInitializeWithFile: IIDType
IID_IInitializeWithStream: IIDType
IID_INamedPropertyStore: IIDType
IID_IObjectWithPropertyKey: IIDType
IID_IPersistSerializedPropStorage: IIDType
IID_IPropertyChange: IIDType
IID_IPropertyChangeArray: IIDType
IID_IPropertyDescription: IIDType
IID_IPropertyDescriptionAliasInfo: IIDType
IID_IPropertyDescriptionList: IIDType
IID_IPropertyDescriptionSearchInfo: IIDType
IID_IPropertyEnumType: IIDType
IID_IPropertyEnumTypeList: IIDType
IID_IPropertyStore: IIDType
IID_IPropertyStoreCache: IIDType
IID_IPropertyStoreCapabilities: IIDType
IID_IPropertySystem: IIDType

@final
class PROPVARIANTType:
    __name__: ClassVar[str] = "PyPROPVARIANT"
    @overload
    @deprecated("Support for passing two ints to create a 64-bit value is deprecated; pass a single int instead")
    def __init__(self, Value: tuple[int, int], Type=...) -> None: ...
    @overload
    def __init__(self, Value, Type=...) -> None: ...
    @property
    def vt(self): ...
    def GetValue(self): ...
    def ToString(self): ...
    def ChangeType(self, Type, Flags: int = ..., /) -> PROPVARIANTType: ...
