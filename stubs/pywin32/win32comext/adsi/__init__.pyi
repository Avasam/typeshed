from _typeshed import Incomplete

import win32com.client
from win32comext.adsi.adsi import *

LCID: int
IDispatchType: Incomplete
IADsContainerType: Incomplete

class ADSIEnumerator:
    index: int
    def __init__(self, ob) -> None: ...
    def __getitem__(self, index): ...
    def __call__(self, index): ...

class ADSIDispatch(win32com.client.CDispatch):
    def __getattr__(self, attr): ...
    def QueryInterface(self, iid): ...
