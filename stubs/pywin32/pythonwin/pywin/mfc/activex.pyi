from _typeshed import Incomplete

from pythonwin.pywin.mfc import window as window

class Control(window.Wnd):
    def __init__(self) -> None: ...
    def CreateControl(self, windowTitle, style, rect, parent, id, lic_string: Incomplete | None = ...) -> None: ...
    def HookOleEvents(self) -> None: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...

def MakeControlClass(controlClass, name: Incomplete | None = ...): ...
def MakeControlInstance(controlClass, name: Incomplete | None = ...): ...
