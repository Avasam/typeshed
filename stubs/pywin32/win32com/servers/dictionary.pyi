from pythoncom import (  # type: ignore[import]  # Crashes stubtest
    DISPATCH_METHOD as DISPATCH_METHOD,
    DISPATCH_PROPERTYGET as DISPATCH_PROPERTYGET,
)
from win32.lib.winerror import S_OK as S_OK
from win32com.server import policy as policy, util as util
from win32com.server.exception import COMException as COMException

class DictionaryPolicy(policy.BasicWrapPolicy): ...

def Register(): ...
