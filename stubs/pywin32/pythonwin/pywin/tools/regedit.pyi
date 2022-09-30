from _typeshed import Incomplete

from pythonwin.pywin.mfc import dialog as dialog, docview as docview, window as window
from pythonwin.pywin.tools import hierlist as hierlist

def SafeApply(fn, args, err_desc: str = ...): ...

class SplitterFrame(window.MDIChildWnd):
    images: Incomplete
    def __init__(self) -> None: ...
    keysview: Incomplete
    valuesview: Incomplete
    def OnCreateClient(self, cp, context): ...
    def OnItemDoubleClick(self, info, extra): ...
    def PerformItemSelected(self, item): ...
    def OnDestroy(self, msg) -> None: ...

class RegistryTreeView(docview.TreeView):
    frame: Incomplete
    hierList: Incomplete
    def OnInitialUpdate(self) -> None: ...
    def GetHLIRoot(self): ...
    def OnItemRightClick(self, notify_data, extra) -> None: ...
    def OnDeleteKey(self, command, code) -> None: ...
    def OnAddKey(self, command, code) -> None: ...
    def OnAddValue(self, command, code) -> None: ...
    def PerformItemSelected(self, item): ...
    def SelectedItem(self): ...
    def SearchSelectedItem(self): ...

class RegistryValueView(docview.ListView):
    def OnInitialUpdate(self) -> None: ...
    def UpdateForRegItem(self, item) -> None: ...
    item: Incomplete
    edit: Incomplete
    newvalue: Incomplete
    def EditValue(self, item): ...
    def GetItemsCurrentValue(self, item, valueName): ...
    def SetItemsCurrentValue(self, item, valueName, value) -> None: ...

class RegTemplate(docview.DocTemplate):
    def __init__(self) -> None: ...
    def OpenRegistryKey(self, root: Incomplete | None = ..., subkey: Incomplete | None = ...): ...

class RegDocument(docview.Document):
    root: Incomplete
    subkey: Incomplete
    def __init__(self, template, root, subkey) -> None: ...
    def OnOpenDocument(self, name): ...

class HLIRegistryKey(hierlist.HierListItem):
    keyRoot: Incomplete
    keyName: Incomplete
    userName: Incomplete
    def __init__(self, keyRoot, keyName, userName) -> None: ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def GetText(self): ...
    def IsExpandable(self): ...
    def GetSubList(self): ...

template: Incomplete

def EditRegistry(root: Incomplete | None = ..., key: Incomplete | None = ...) -> None: ...
