from _typeshed import Incomplete
from typing import Any

# from win32.lib.pywintypes import IID  # Crashes stubtest
from typing_extensions import TypeAlias

IID: TypeAlias = Incomplete

IID_ISecurityInformation: IID

def EditSecurity(*args, **kwargs) -> Any: ...
