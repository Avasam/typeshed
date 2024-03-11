from _typeshed import Incomplete
from typing_extensions import TypeAlias

import _win32typing
from win32.lib.pywintypes import IIDType, SECURITY_DESCRIPTORType, com_error as com_error

error: TypeAlias = com_error  # noqa: Y042

class internal_error(Exception): ...

def CoCreateFreeThreadedMarshaler(unk: _win32typing.PyIUnknown, /) -> _win32typing.PyIUnknown: ...
def CoCreateInstanceEx(
    clsid: IIDType,
    unkOuter: _win32typing.PyIUnknown,
    context,
    serverInfo: tuple[Incomplete, Incomplete, Incomplete, Incomplete],
    iids: list[IIDType],
    /,
) -> _win32typing.PyIUnknown: ...
def CoCreateInstance(
    clsid: IIDType, unkOuter: _win32typing.PyIUnknown | None, context: int, iid: IIDType, /
) -> _win32typing.PyIUnknown: ...
def CoFreeUnusedLibraries() -> None: ...
def CoInitialize() -> None: ...
def CoInitializeEx(flags, /) -> None: ...
def CoInitializeSecurity(
    sd: SECURITY_DESCRIPTORType, authSvc, reserved1, authnLevel, impLevel, authInfo, capabilities, reserved2, /
) -> None: ...
def CoGetInterfaceAndReleaseStream(stream: _win32typing.PyIStream, iid: IIDType, /) -> _win32typing.PyIUnknown: ...
def CoMarshalInterThreadInterfaceInStream(iid: IIDType, unk: _win32typing.PyIUnknown, /) -> _win32typing.PyIStream: ...
def CoMarshalInterface(
    Stm: _win32typing.PyIStream, riid: IIDType, Unk: _win32typing.PyIUnknown, DestContext, flags, /
) -> None: ...
def CoUnmarshalInterface(Stm: _win32typing.PyIStream, riid: IIDType, /): ...
def CoReleaseMarshalData(Stm: _win32typing.PyIStream, /) -> None: ...
def CoGetObject(name: str, iid: IIDType, bindOpts: Incomplete | None = ..., /) -> _win32typing.PyIUnknown: ...
def CoUninitialize() -> None: ...
def CoRegisterClassObject(iid: IIDType, factory: _win32typing.PyIUnknown, context, flags, /): ...
def CoResumeClassObjects() -> None: ...
def CoRevokeClassObject(reg, /) -> None: ...
def CoTreatAsClass(clsidold: IIDType, clsidnew: IIDType, /) -> None: ...
def CoWaitForMultipleHandles(Flags, Timeout, Handles: list[int], /): ...
def Connect(cls, /) -> _win32typing.PyIDispatch: ...
def connect(*args): ...  # incomplete
def CreateGuid() -> IIDType: ...
def CreateBindCtx() -> _win32typing.PyIBindCtx: ...
def CreateFileMoniker(filename: str, /) -> _win32typing.PyIMoniker: ...
def CreateItemMoniker(delim: str, item: str, /) -> _win32typing.PyIMoniker: ...
def CreatePointerMoniker(IUnknown: _win32typing.PyIUnknown, /) -> _win32typing.PyIMoniker: ...
def CreateURLMonikerEx(*args): ...  # incomplete
def CreateTypeLib(): ...
def CreateTypeLib2(): ...
def CreateStreamOnHGlobal(hGlobal: int | None = ..., DeleteOnRelease: bool = ..., /) -> _win32typing.PyIStream: ...
def CreateILockBytesOnHGlobal(hGlobal: int | None = ..., DeleteOnRelease: bool = ..., /) -> _win32typing.PyILockBytes: ...
def EnableQuitMessage(threadId, /) -> None: ...
def FUNCDESC() -> _win32typing.FUNCDESC: ...
def GetActiveObject(cls, /) -> _win32typing.PyIUnknown: ...
def GetClassFile(fileName, /) -> IIDType: ...
def GetFacilityString(scode, /) -> str: ...
def GetRecordFromGuids(iid: IIDType, verMajor, verMinor, lcid, infoIID: IIDType, data: Incomplete | None = ..., /): ...
def GetRecordFromTypeInfo(TypeInfo: _win32typing.PyITypeInfo, /): ...
def GetRunningObjectTable(reserved: int = ..., /) -> _win32typing.PyIRunningObjectTable: ...
def GetScodeString(scode, /) -> str: ...
def GetScodeRangeString(scode, /) -> str: ...
def GetSeverityString(scode, /) -> str: ...
def IsGatewayRegistered(iid: IIDType | None, /) -> int: ...
def LoadRegTypeLib(iid: IIDType, versionMajor, versionMinor, lcid, /) -> _win32typing.PyITypeLib: ...
def LoadTypeLib(libFileName: str, /) -> _win32typing.PyITypeLib: ...
def MakePyFactory(iid: IIDType, /) -> _win32typing.PyIClassFactory: ...
def MkParseDisplayName(
    displayName: str, bindCtx: _win32typing.PyIBindCtx | None = ..., /
) -> tuple[_win32typing.PyIMoniker, Incomplete, _win32typing.PyIBindCtx]: ...
def new(iid: IIDType | str, /): ...
def New(cls, /) -> _win32typing.PyIDispatch: ...
def ObjectFromAddress(address, iid: IIDType, /) -> _win32typing.PyIUnknown: ...
def ObjectFromLresult(lresult, iid: IIDType, wparm, /) -> _win32typing.PyIUnknown: ...
def OleInitialize() -> None: ...
def OleGetClipboard() -> _win32typing.PyIDataObject: ...
def OleFlushClipboard() -> None: ...
def OleIsCurrentClipboard(dataObj: _win32typing.PyIDataObject, /): ...
def OleSetClipboard(dataObj: _win32typing.PyIDataObject, /) -> None: ...
def OleLoadFromStream(stream: _win32typing.PyIStream, iid: IIDType, /) -> None: ...
def OleSaveToStream(persist: _win32typing.PyIPersistStream, stream: _win32typing.PyIStream, /) -> None: ...
def OleLoad(storage: _win32typing.PyIStorage, iid: IIDType, site: _win32typing.PyIOleClientSite, /) -> None: ...
def ProgIDFromCLSID(clsid, /) -> str: ...
def PumpWaitingMessages(firstMessage: int = ..., lastMessage: int = ..., /) -> int: ...
def PumpMessages() -> None: ...
def QueryPathOfRegTypeLib(iid: IIDType, versionMajor, versionMinor, lcid, /) -> str: ...
def ReadClassStg(storage: _win32typing.PyIStorage, /) -> IIDType: ...
def ReadClassStm(Stm: _win32typing.PyIStream, /) -> IIDType: ...
def RegisterTypeLib(typelib: _win32typing.PyITypeLib, fullPath: str, lcid, helpDir: str | None = ..., /) -> None: ...
def UnRegisterTypeLib(iid: IIDType, versionMajor, versionMinor, lcid, syskind, /) -> str: ...
def RegisterActiveObject(obUnknown: _win32typing.PyIUnknown, clsid: IIDType, flags, /): ...
def RevokeActiveObject(handle, /) -> None: ...
def RegisterDragDrop(hwnd: int, dropTarget: _win32typing.PyIDropTarget, /) -> None: ...
def RevokeDragDrop(hwnd: int, /) -> None: ...
def DoDragDrop() -> None: ...
def StgCreateDocfile(name: str, mode, reserved: int = ..., /) -> _win32typing.PyIStorage: ...
def StgCreateDocfileOnILockBytes(lockBytes: _win32typing.PyILockBytes, mode, reserved=..., /) -> _win32typing.PyIStorage: ...
def StgOpenStorageOnILockBytes(
    lockBytes: _win32typing.PyILockBytes,
    stgPriority: _win32typing.PyIStorage,
    snbExclude: Incomplete | None = ...,
    reserved: int = ...,
    /,
) -> _win32typing.PyIStorage: ...
def StgIsStorageFile(name: str, /): ...
def STGMEDIUM() -> _win32typing.PySTGMEDIUM: ...
def StgOpenStorage(
    name: str, other: _win32typing.PyIStorage, mode, snbExclude: Incomplete | None = ..., reserved=..., /
) -> _win32typing.PyIStorage: ...
def StgOpenStorageEx(
    Name: str, Mode, stgfmt, Attrs, riid: IIDType, StgOptions: Incomplete | None = ...
) -> _win32typing.PyIStorage: ...
def StgCreateStorageEx(
    Name: str,
    Mode,
    stgfmt,
    Attrs,
    riid: IIDType,
    StgOptions: Incomplete | None = ...,
    SecurityDescriptor: SECURITY_DESCRIPTORType | None = ...,
) -> _win32typing.PyIStorage: ...
def TYPEATTR() -> _win32typing.TYPEATTR: ...
def VARDESC() -> _win32typing.VARDESC: ...
def WrapObject(ob, gatewayIID: IIDType, interfaceIID: IIDType, /) -> _win32typing.PyIUnknown: ...
def WriteClassStg(storage: _win32typing.PyIStorage, iid: IIDType, /) -> None: ...
def WriteClassStm(Stm: _win32typing.PyIStream, clsid: IIDType, /) -> None: ...
def UnwrapObject(ob: _win32typing.PyIUnknown, /) -> _win32typing.PyIDispatch: ...
def FmtIdToPropStgName(fmtid: IIDType, /): ...
def PropStgNameToFmtId(Name: str, /) -> IIDType: ...
def CoGetCallContext(riid: IIDType, /) -> _win32typing.PyIServerSecurity: ...
def CoGetObjectContext(riid: IIDType, /) -> _win32typing.PyIContext: ...
def CoGetCancelObject(riid: IIDType, ThreadID: int = ..., /) -> _win32typing.PyICancelMethodCalls: ...
def CoSetCancelObject(Unk: _win32typing.PyIUnknown, /) -> None: ...
def CoEnableCallCancellation() -> None: ...
def CoDisableCallCancellation() -> None: ...

ACTIVEOBJECT_STRONG: int
ACTIVEOBJECT_WEAK: int
ArgNotFound: _win32typing.ArgNotFound
CLSCTX_ALL: int
CLSCTX_INPROC: int
CLSCTX_INPROC_HANDLER: int
CLSCTX_INPROC_SERVER: int
CLSCTX_LOCAL_SERVER: int
CLSCTX_REMOTE_SERVER: int
CLSCTX_SERVER: int
CLSID_DCOMAccessControl: IIDType
CLSID_StdComponentCategoriesMgr: IIDType
CLSID_StdGlobalInterfaceTable: IIDType
COINIT_APARTMENTTHREADED: int
COINIT_DISABLE_OLE1DDE: int
COINIT_MULTITHREADED: int
COINIT_SPEED_OVER_MEMORY: int
COWAIT_ALERTABLE: int
COWAIT_WAITALL: int
DATADIR_GET: int
DATADIR_SET: int
DESCKIND_FUNCDESC: int
DESCKIND_VARDESC: int
DISPATCH_METHOD: int
DISPATCH_PROPERTYGET: int
DISPATCH_PROPERTYPUT: int
DISPATCH_PROPERTYPUTREF: int
DISPID_COLLECT: int
DISPID_CONSTRUCTOR: int
DISPID_DESTRUCTOR: int
DISPID_EVALUATE: int
DISPID_NEWENUM: int
DISPID_PROPERTYPUT: int
DISPID_STARTENUM: int
DISPID_THIS: int
DISPID_UNKNOWN: int
DISPID_VALUE: int
DVASPECT_CONTENT: int
DVASPECT_DOCPRINT: int
DVASPECT_ICON: int
DVASPECT_THUMBNAIL: int
EOAC_ACCESS_CONTROL: int
EOAC_ANY_AUTHORITY: int
EOAC_APPID: int
EOAC_AUTO_IMPERSONATE: int
EOAC_DEFAULT: int
EOAC_DISABLE_AAA: int
EOAC_DYNAMIC: int
EOAC_DYNAMIC_CLOAKING: int
EOAC_MAKE_FULLSIC: int
EOAC_MUTUAL_AUTH: int
EOAC_NONE: int
EOAC_NO_CUSTOM_MARSHAL: int
EOAC_REQUIRE_FULLSIC: int
EOAC_SECURE_REFS: int
EOAC_STATIC_CLOAKING: int
EXTCONN_CALLABLE: int
EXTCONN_STRONG: int
EXTCONN_WEAK: int
Empty: _win32typing.PyOleEmpty
FMTID_DocSummaryInformation: IIDType
FMTID_SummaryInformation: IIDType
FMTID_UserDefinedProperties: IIDType
FUNCFLAG_FBINDABLE: int
FUNCFLAG_FDEFAULTBIND: int
FUNCFLAG_FDISPLAYBIND: int
FUNCFLAG_FHIDDEN: int
FUNCFLAG_FREQUESTEDIT: int
FUNCFLAG_FRESTRICTED: int
FUNCFLAG_FSOURCE: int
FUNCFLAG_FUSESGETLASTERROR: int
FUNC_DISPATCH: int
FUNC_NONVIRTUAL: int
FUNC_PUREVIRTUAL: int
FUNC_STATIC: int
FUNC_VIRTUAL: int
IDLFLAG_FIN: int
IDLFLAG_FLCID: int
IDLFLAG_FOUT: int
IDLFLAG_FRETVAL: int
IDLFLAG_NONE: int
IID_IBindCtx: IIDType
IID_ICancelMethodCalls: IIDType
IID_ICatInformation: IIDType
IID_ICatRegister: IIDType
IID_IClassFactory: IIDType
IID_IClientSecurity: IIDType
IID_IConnectionPoint: IIDType
IID_IConnectionPointContainer: IIDType
IID_IContext: IIDType
IID_ICreateTypeInfo: IIDType
IID_ICreateTypeLib: IIDType
IID_ICreateTypeLib2: IIDType
IID_IDataObject: IIDType
IID_IDispatch: IIDType
IID_IDispatchEx: IIDType
IID_IDropSource: IIDType
IID_IDropTarget: IIDType
IID_IEnumCATEGORYINFO: IIDType
IID_IEnumConnectionPoints: IIDType
IID_IEnumConnections: IIDType
IID_IEnumContextProps: IIDType
IID_IEnumFORMATETC: IIDType
IID_IEnumGUID: IIDType
IID_IEnumMoniker: IIDType
IID_IEnumSTATPROPSETSTG: IIDType
IID_IEnumSTATPROPSTG: IIDType
IID_IEnumSTATSTG: IIDType
IID_IEnumString: IIDType
IID_IEnumVARIANT: IIDType
IID_IErrorLog: IIDType
IID_IExternalConnection: IIDType
IID_IGlobalInterfaceTable: IIDType
IID_ILockBytes: IIDType
IID_IMarshal: IIDType
IID_IMoniker: IIDType
IID_IOleWindow: IIDType
IID_IPersist: IIDType
IID_IPersistFile: IIDType
IID_IPersistPropertyBag: IIDType
IID_IPersistStorage: IIDType
IID_IPersistStream: IIDType
IID_IPersistStreamInit: IIDType
IID_IPropertyBag: IIDType
IID_IPropertySetStorage: IIDType
IID_IPropertyStorage: IIDType
IID_IProvideClassInfo: IIDType
IID_IProvideClassInfo2: IIDType
IID_IRunningObjectTable: IIDType
IID_IServerSecurity: IIDType
IID_IServiceProvider: IIDType
IID_IStdMarshalInfo: IIDType
IID_IStorage: IIDType
IID_IStream: IIDType
IID_ITypeComp: IIDType
IID_ITypeInfo: IIDType
IID_ITypeLib: IIDType
IID_IUnknown: IIDType
IID_NULL: IIDType
IID_StdOle: IIDType
IMPLTYPEFLAG_FDEFAULT: int
IMPLTYPEFLAG_FRESTRICTED: int
IMPLTYPEFLAG_FSOURCE: int
INVOKE_FUNC: int
INVOKE_PROPERTYGET: int
INVOKE_PROPERTYPUT: int
INVOKE_PROPERTYPUTREF: int
InterfaceNames: dict[str, IIDType]
MKSYS_ANTIMONIKER: int
MKSYS_CLASSMONIKER: int
MKSYS_FILEMONIKER: int
MKSYS_GENERICCOMPOSITE: int
MKSYS_ITEMMONIKER: int
MKSYS_NONE: int
MKSYS_POINTERMONIKER: int
MSHCTX_DIFFERENTMACHINE: int
MSHCTX_INPROC: int
MSHCTX_LOCAL: int
MSHCTX_NOSHAREDMEM: int
MSHLFLAGS_NOPING: int
MSHLFLAGS_NORMAL: int
MSHLFLAGS_TABLESTRONG: int
MSHLFLAGS_TABLEWEAK: int
Missing: _win32typing.PyOleMissing
Nothing: _win32typing.PyOleNothing
PARAMFLAG_FHASDEFAULT: int
PARAMFLAG_FIN: int
PARAMFLAG_FLCID: int
PARAMFLAG_FOPT: int
PARAMFLAG_FOUT: int
PARAMFLAG_FRETVAL: int
PARAMFLAG_NONE: int
REGCLS_MULTIPLEUSE: int
REGCLS_MULTI_SEPARATE: int
REGCLS_SINGLEUSE: int
REGCLS_SUSPENDED: int
ROTFLAGS_ALLOWANYCLIENT: int
ROTFLAGS_REGISTRATIONKEEPSALIVE: int
RPC_C_AUTHN_DCE_PRIVATE: int
RPC_C_AUTHN_DCE_PUBLIC: int
RPC_C_AUTHN_DEC_PUBLIC: int
RPC_C_AUTHN_DEFAULT: int
RPC_C_AUTHN_DPA: int
RPC_C_AUTHN_GSS_KERBEROS: int
RPC_C_AUTHN_GSS_NEGOTIATE: int
RPC_C_AUTHN_GSS_SCHANNEL: int
RPC_C_AUTHN_LEVEL_CALL: int
RPC_C_AUTHN_LEVEL_CONNECT: int
RPC_C_AUTHN_LEVEL_DEFAULT: int
RPC_C_AUTHN_LEVEL_NONE: int
RPC_C_AUTHN_LEVEL_PKT: int
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY: int
RPC_C_AUTHN_LEVEL_PKT_PRIVACY: int
RPC_C_AUTHN_MQ: int
RPC_C_AUTHN_MSN: int
RPC_C_AUTHN_NONE: int
RPC_C_AUTHN_WINNT: int
RPC_C_AUTHZ_DCE: int
RPC_C_AUTHZ_DEFAULT: int
RPC_C_AUTHZ_NAME: int
RPC_C_AUTHZ_NONE: int
RPC_C_IMP_LEVEL_ANONYMOUS: int
RPC_C_IMP_LEVEL_DEFAULT: int
RPC_C_IMP_LEVEL_DELEGATE: int
RPC_C_IMP_LEVEL_IDENTIFY: int
RPC_C_IMP_LEVEL_IMPERSONATE: int
STDOLE2_LCID: int
STDOLE2_MAJORVERNUM: int
STDOLE2_MINORVERNUM: int
STDOLE_LCID: int
STDOLE_MAJORVERNUM: int
STDOLE_MINORVERNUM: int
STREAM_SEEK_CUR: int
STREAM_SEEK_END: int
STREAM_SEEK_SET: int
SYS_MAC: int
SYS_WIN16: int
SYS_WIN32: int
ServerInterfaces: dict[IIDType, bytes]
TKIND_ALIAS: int
TKIND_COCLASS: int
TKIND_DISPATCH: int
TKIND_ENUM: int
TKIND_INTERFACE: int
TKIND_MODULE: int
TKIND_RECORD: int
TKIND_UNION: int
TYMED_ENHMF: int
TYMED_FILE: int
TYMED_GDI: int
TYMED_HGLOBAL: int
TYMED_ISTORAGE: int
TYMED_ISTREAM: int
TYMED_MFPICT: int
TYMED_NULL: int
TYPEFLAG_FAGGREGATABLE: int
TYPEFLAG_FAPPOBJECT: int
TYPEFLAG_FCANCREATE: int
TYPEFLAG_FCONTROL: int
TYPEFLAG_FDISPATCHABLE: int
TYPEFLAG_FDUAL: int
TYPEFLAG_FHIDDEN: int
TYPEFLAG_FLICENSED: int
TYPEFLAG_FNONEXTENSIBLE: int
TYPEFLAG_FOLEAUTOMATION: int
TYPEFLAG_FPREDECLID: int
TYPEFLAG_FREPLACEABLE: int
TYPEFLAG_FRESTRICTED: int
TYPEFLAG_FREVERSEBIND: int
TypeIIDs: dict[IIDType, type]
URL_MK_LEGACY: int
URL_MK_UNIFORM: int
VARFLAG_FREADONLY: int
VAR_CONST: int
VAR_DISPATCH: int
VAR_PERINSTANCE: int
VAR_STATIC: int
VT_ARRAY: int
VT_BLOB: int
VT_BLOB_OBJECT: int
VT_BOOL: int
VT_BSTR: int
VT_BSTR_BLOB: int
VT_BYREF: int
VT_CARRAY: int
VT_CF: int
VT_CLSID: int
VT_CY: int
VT_DATE: int
VT_DECIMAL: int
VT_DISPATCH: int
VT_EMPTY: int
VT_ERROR: int
VT_FILETIME: int
VT_HRESULT: int
VT_I1: int
VT_I2: int
VT_I4: int
VT_I8: int
VT_ILLEGAL: int
VT_ILLEGALMASKED: int
VT_INT: int
VT_LPSTR: int
VT_LPWSTR: int
VT_NULL: int
VT_PTR: int
VT_R4: int
VT_R8: int
VT_RECORD: int
VT_RESERVED: int
VT_SAFEARRAY: int
VT_STORAGE: int
VT_STORED_OBJECT: int
VT_STREAM: int
VT_STREAMED_OBJECT: int
VT_TYPEMASK: int
VT_UI1: int
VT_UI2: int
VT_UI4: int
VT_UI8: int
VT_UINT: int
VT_UNKNOWN: int
VT_USERDEFINED: int
VT_VARIANT: int
VT_VECTOR: int
VT_VOID: int

dcom: int
fdexNameCaseInsensitive: int
fdexNameCaseSensitive: int
fdexNameEnsure: int
fdexNameImplicit: int
fdexPropCanCall: int
fdexPropCanConstruct: int
fdexPropCanGet: int
fdexPropCanPut: int
fdexPropCanPutRef: int
fdexPropCanSourceEvents: int
fdexPropCannotCall: int
fdexPropCannotConstruct: int
fdexPropCannotGet: int
fdexPropCannotPut: int
fdexPropCannotPutRef: int
fdexPropCannotSourceEvents: int
fdexPropDynamicType: int
fdexPropNoSideEffects: int
frozen: int
