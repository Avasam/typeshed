from typing import Any
from typing_extensions import final

@final
class NCB:
    Bufflen: Any
    Callname: Any
    Cmd_cplt: Any
    Command: Any
    Event: Any
    Lana_num: Any
    Lsn: Any
    Name: Any
    Num: Any
    Post: Any
    Retcode: Any
    Rto: Any
    Sto: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def Reset(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class NCBType:
    Bufflen: Any
    Callname: Any
    Cmd_cplt: Any
    Command: Any
    Event: Any
    Lana_num: Any
    Lsn: Any
    Name: Any
    Num: Any
    Post: Any
    Retcode: Any
    Rto: Any
    Sto: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def Reset(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class NETRESOURCE:
    dwDisplayType: Any
    dwScope: Any
    dwType: Any
    dwUsage: Any
    lpComment: Any
    lpLocalName: Any
    lpProvider: Any
    lpRemoteName: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class NETRESOURCEType:
    dwDisplayType: Any
    dwScope: Any
    dwType: Any
    dwUsage: Any
    lpComment: Any
    lpLocalName: Any
    lpProvider: Any
    lpRemoteName: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class error(Exception): ...

def NCBBuffer(*args, **kwargs) -> Any: ...
def Netbios(*args, **kwargs) -> Any: ...
def WNetAddConnection2(NetResource, Password, UserName, Flags) -> Any: ...
def WNetAddConnection3(HwndParent, NetResource, Password, UserName, Flags) -> Any: ...
def WNetCancelConnection2(*args, **kwargs) -> Any: ...
def WNetCloseEnum(*args, **kwargs) -> Any: ...
def WNetEnumResource(*args, **kwargs) -> Any: ...
def WNetGetConnection(*args, **kwargs) -> Any: ...
def WNetGetLastError(*args, **kwargs) -> Any: ...
def WNetGetResourceInformation(*args, **kwargs) -> Any: ...
def WNetGetResourceParent(*args, **kwargs) -> Any: ...
def WNetGetUniversalName(*args, **kwargs) -> Any: ...
def WNetGetUser(*args, **kwargs) -> Any: ...
def WNetOpenEnum(*args, **kwargs) -> Any: ...
