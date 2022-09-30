from _typeshed import Incomplete

from pythonwin.pywin.mfc import dialog

class RegistryControl:
    key: Incomplete
    def __init__(self, key) -> None: ...

class RegEditPropertyPage(dialog.PropertyPage):
    IDC_LISTVIEW: int
    def GetTemplate(self): ...

class RegistryPage(RegEditPropertyPage):
    caption: str
    def __init__(self) -> None: ...
    listview: Incomplete
    def OnInitDialog(self) -> None: ...

class RegistrySheet(dialog.PropertySheet):
    def __init__(self, title) -> None: ...
    def OnActivate(self, msg) -> None: ...

def t() -> None: ...
