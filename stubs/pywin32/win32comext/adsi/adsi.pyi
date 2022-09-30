from _typeshed import Incomplete
from typing import Any
from typing_extensions import TypeAlias

# from win32.lib.pywintypes import IID  # Crashes stubtest
IID: TypeAlias = Incomplete

CLSID_ADsDSOObject: IID
CLSID_AccessControlEntry: IID
CLSID_AccessControlList: IID
CLSID_DsObjectPicker: IID
CLSID_SecurityDescriptor: IID
DBGUID_LDAPDialect: IID
DBPROPSET_ADSISEARCH: IID
IID_IADs: IID
IID_IADsClass: IID
IID_IADsCollection: IID
IID_IADsComputer: IID
IID_IADsComputerOperations: IID
IID_IADsContainer: IID
IID_IADsDeleteOps: IID
IID_IADsDomain: IID
IID_IADsFileService: IID
IID_IADsFileServiceOperations: IID
IID_IADsFileShare: IID
IID_IADsGroup: IID
IID_IADsLocality: IID
IID_IADsMembers: IID
IID_IADsNamespaces: IID
IID_IADsO: IID
IID_IADsOU: IID
IID_IADsOpenDSObject: IID
IID_IADsPrintJob: IID
IID_IADsPrintJobOperations: IID
IID_IADsPrintQueue: IID
IID_IADsPrintQueueOperations: IID
IID_IADsProperty: IID
IID_IADsPropertyList: IID
IID_IADsResource: IID
IID_IADsSearch: IID
IID_IADsService: IID
IID_IADsServiceOperations: IID
IID_IADsSession: IID
IID_IADsSyntax: IID
IID_IADsUser: IID
IID_IDirectoryObject: IID
IID_IDirectorySearch: IID
IID_IDsObjectPicker: IID
LIBID_ADs: IID

class DSOP_SCOPE_INIT_INFOs:
    def __init__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, name) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class error(Exception): ...

def ADsBuildEnumerator(*args, **kwargs) -> Any: ...
def ADsEnumerateNext(*args, **kwargs) -> Any: ...
def ADsGetLastError(*args, **kwargs) -> Any: ...
def ADsGetObject(path, iid=...): ...
def ADsOpenObject(path, username, password, reserved: int = ..., iid=...): ...
def StringAsDS_SELECTION_LIST(*args, **kwargs) -> Any: ...
