from _typeshed import Incomplete
from typing_extensions import TypeAlias

from pythonwin.pywin.mfc import dialog

class TLBrowserException(Exception): ...

error = TLBrowserException
FRAMEDLG_STD: Incomplete
SS_STD: Incomplete
BS_STD: Incomplete
ES_STD: Incomplete
LBS_STD: Incomplete
CBS_STD: Incomplete
typekindmap: Incomplete
TypeBrowseDialog_Parent: TypeAlias = dialog.Dialog

class TypeBrowseDialog(TypeBrowseDialog_Parent):
    IDC_TYPELIST: int
    IDC_MEMBERLIST: int
    IDC_PARAMLIST: int
    IDC_LISTVIEW: int
    tlb: Incomplete
    def __init__(self, typefile: Incomplete | None = ...) -> None: ...
    typeinfo: Incomplete
    attr: Incomplete
    def OnAttachedObjectDeath(self): ...
    def OnFileOpen(self, id, code) -> None: ...
    typelb: Incomplete
    memberlb: Incomplete
    paramlb: Incomplete
    listview: Incomplete
    def OnInitDialog(self): ...
    def SetupAllInfoTypes(self) -> None: ...
    def CmdTypeListbox(self, id, code): ...
    def CmdMemberListbox(self, id, code): ...
    def GetTemplate(self): ...
