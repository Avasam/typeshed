from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import TypeAlias

from win32.lib.pywintypes import IIDType, com_error
from win32comext.adsi import IADsContainerType

error: TypeAlias = com_error  # noqa: Y042

def ADsOpenObject(path, username, password, iid: IIDType, reserved: int = ..., /): ...
def ADsGetObject(path, iid: IIDType, /): ...
def ADsBuildEnumerator(container: IADsContainerType, /): ...
def ADsEnumerateNext(enum, num: int = ..., /): ...
def ADsGetLastError() -> tuple[Incomplete, Incomplete, Incomplete]: ...
def StringAsDS_SELECTION_LIST(*args): ...  # incomplete

class DSOP_SCOPE_INIT_INFOs:
    __name__: ClassVar[str] = "PyDSOP_SCOPE_INIT_INFOs"
    def __new__(cls, size, /): ...

CLSID_ADsDSOObject: IIDType
CLSID_AccessControlEntry: IIDType
CLSID_AccessControlList: IIDType
CLSID_DsObjectPicker: IIDType
CLSID_SecurityDescriptor: IIDType
DBGUID_LDAPDialect: IIDType
DBPROPSET_ADSISEARCH: IIDType
IID_IADs: IIDType
IID_IADsClass: IIDType
IID_IADsCollection: IIDType
IID_IADsComputer: IIDType
IID_IADsComputerOperations: IIDType
IID_IADsContainer: IIDType
IID_IADsDeleteOps: IIDType
IID_IADsDomain: IIDType
IID_IADsFileService: IIDType
IID_IADsFileServiceOperations: IIDType
IID_IADsFileShare: IIDType
IID_IADsGroup: IIDType
IID_IADsLocality: IIDType
IID_IADsMembers: IIDType
IID_IADsNamespaces: IIDType
IID_IADsO: IIDType
IID_IADsOU: IIDType
IID_IADsOpenDSObject: IIDType
IID_IADsPrintJob: IIDType
IID_IADsPrintJobOperations: IIDType
IID_IADsPrintQueue: IIDType
IID_IADsPrintQueueOperations: IIDType
IID_IADsProperty: IIDType
IID_IADsPropertyList: IIDType
IID_IADsResource: IIDType
IID_IADsSearch: IIDType
IID_IADsService: IIDType
IID_IADsServiceOperations: IIDType
IID_IADsSession: IIDType
IID_IADsSyntax: IIDType
IID_IADsUser: IIDType
IID_IDirectoryObject: IIDType
IID_IDirectorySearch: IIDType
IID_IDsObjectPicker: IIDType
LIBID_ADs: IIDType
