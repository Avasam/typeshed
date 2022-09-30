from _typeshed import Incomplete

from win32com.server.policy import DynamicPolicy
from win32comext.axscript import axscript as axscript

debugging: int
PyIDispatchType: Incomplete

class ScriptDispatch:
    engine: Incomplete
    scriptNamespace: Incomplete
    def __init__(self, engine, scriptNamespace) -> None: ...

class StrictDynamicPolicy(DynamicPolicy): ...

def MakeScriptDispatch(engine, namespace): ...
