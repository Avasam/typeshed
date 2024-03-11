from typing import ClassVar, NoReturn, final
from typing_extensions import Never, TypeAlias, deprecated

import _win32typing
import win32com.client
from win32.lib.pywintypes import IIDType
from win32comext.adsi.adsi import (
    DBPROPSET_ADSISEARCH as DBPROPSET_ADSISEARCH,
    ADsBuildEnumerator as ADsBuildEnumerator,
    ADsEnumerateNext as ADsEnumerateNext,
    ADsGetLastError as ADsGetLastError,
    CLSID_AccessControlEntry as CLSID_AccessControlEntry,
    CLSID_AccessControlList as CLSID_AccessControlList,
    CLSID_ADsDSOObject as CLSID_ADsDSOObject,
    CLSID_DsObjectPicker as CLSID_DsObjectPicker,
    CLSID_SecurityDescriptor as CLSID_SecurityDescriptor,
    DBGUID_LDAPDialect as DBGUID_LDAPDialect,
    DSOP_SCOPE_INIT_INFOs as DSOP_SCOPE_INIT_INFOs,
    IID_IADs as IID_IADs,
    IID_IADsClass as IID_IADsClass,
    IID_IADsCollection as IID_IADsCollection,
    IID_IADsComputer as IID_IADsComputer,
    IID_IADsComputerOperations as IID_IADsComputerOperations,
    IID_IADsContainer as IID_IADsContainer,
    IID_IADsDeleteOps as IID_IADsDeleteOps,
    IID_IADsDomain as IID_IADsDomain,
    IID_IADsFileService as IID_IADsFileService,
    IID_IADsFileServiceOperations as IID_IADsFileServiceOperations,
    IID_IADsFileShare as IID_IADsFileShare,
    IID_IADsGroup as IID_IADsGroup,
    IID_IADsLocality as IID_IADsLocality,
    IID_IADsMembers as IID_IADsMembers,
    IID_IADsNamespaces as IID_IADsNamespaces,
    IID_IADsO as IID_IADsO,
    IID_IADsOpenDSObject as IID_IADsOpenDSObject,
    IID_IADsOU as IID_IADsOU,
    IID_IADsPrintJob as IID_IADsPrintJob,
    IID_IADsPrintJobOperations as IID_IADsPrintJobOperations,
    IID_IADsPrintQueue as IID_IADsPrintQueue,
    IID_IADsPrintQueueOperations as IID_IADsPrintQueueOperations,
    IID_IADsProperty as IID_IADsProperty,
    IID_IADsPropertyList as IID_IADsPropertyList,
    IID_IADsResource as IID_IADsResource,
    IID_IADsSearch as IID_IADsSearch,
    IID_IADsService as IID_IADsService,
    IID_IADsServiceOperations as IID_IADsServiceOperations,
    IID_IADsSession as IID_IADsSession,
    IID_IADsSyntax as IID_IADsSyntax,
    IID_IADsUser as IID_IADsUser,
    IID_IDirectoryObject as IID_IDirectoryObject,
    IID_IDirectorySearch as IID_IDirectorySearch,
    IID_IDsObjectPicker as IID_IDsObjectPicker,
    LIBID_ADs as LIBID_ADs,
    StringAsDS_SELECTION_LIST as StringAsDS_SELECTION_LIST,
)

LCID: int
IDispatchType: TypeAlias = _win32typing.PyIDispatch

@final
class IADsContainerType:
    __name__: ClassVar[str] = "PyIADsContainer"
    @deprecated("Cannot create 'PyIADsContainer' instances.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    def GetObject(self, _class: str, relativeName: str, /) -> _win32typing.PyIDispatch: ...
    def get_Count(self): ...
    def get_Filter(self): ...
    def put_Filter(self, val, /) -> None: ...
    def get_Hints(self): ...
    def put_Hints(self, val, /) -> None: ...

class ADSIEnumerator:
    index: int
    def __init__(self, ob) -> None: ...
    def __getitem__(self, index): ...
    def __call__(self, index): ...

class ADSIDispatch(win32com.client.CDispatch):
    def __getattr__(self, attr: str): ...
    def QueryInterface(self, iid): ...

# Redefinition making "iid" optional.
def ADsGetObject(path, iid: IIDType = ...): ...

# Redefinition with flipped "reserved" and "iid" arguments.
def ADsOpenObject(path, username, password, reserved: int = ..., iid: IIDType = ...): ...
