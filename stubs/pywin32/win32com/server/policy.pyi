from _typeshed import Incomplete

from pythoncom import (  # type: ignore[import]  # Crashes stubtests
    DISPATCH_METHOD as DISPATCH_METHOD,
    DISPATCH_PROPERTYGET as DISPATCH_PROPERTYGET,
    DISPATCH_PROPERTYPUT as DISPATCH_PROPERTYPUT,
    DISPATCH_PROPERTYPUTREF as DISPATCH_PROPERTYPUTREF,
    DISPID_COLLECT as DISPID_COLLECT,
    DISPID_CONSTRUCTOR as DISPID_CONSTRUCTOR,
    DISPID_DESTRUCTOR as DISPID_DESTRUCTOR,
    DISPID_EVALUATE as DISPID_EVALUATE,
    DISPID_NEWENUM as DISPID_NEWENUM,
    DISPID_PROPERTYPUT as DISPID_PROPERTYPUT,
    DISPID_STARTENUM as DISPID_STARTENUM,
    DISPID_UNKNOWN as DISPID_UNKNOWN,
    DISPID_VALUE as DISPID_VALUE,
)
from win32com.server.dispatcher import DispatcherTrace as DispatcherTrace, DispatcherWin32trace as DispatcherWin32trace
from win32com.server.exception import COMException as COMException

S_OK: int
IDispatchType: Incomplete
IUnknownType: Incomplete
error: Incomplete
regSpec: str
regPolicy: str
regDispatcher: str
regAddnPath: str

def CreateInstance(clsid, reqIID): ...

class BasicWrapPolicy:
    def __init__(self, object) -> None: ...

class MappedWrapPolicy(BasicWrapPolicy): ...
class DesignatedWrapPolicy(MappedWrapPolicy): ...
class EventHandlerPolicy(DesignatedWrapPolicy): ...
class DynamicPolicy(BasicWrapPolicy): ...

DefaultPolicy = DesignatedWrapPolicy

def resolve_func(spec): ...
def call_func(spec, *args): ...
