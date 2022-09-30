from . import pyscript as pyscript
from .pyscript import (
    SCRIPTTEXT_FORCEEXECUTION as SCRIPTTEXT_FORCEEXECUTION,
    Exception as Exception,
    RaiseAssert as RaiseAssert,
    trace as trace,
)

PyDump_CLSID: str

class AXScriptAttribute(pyscript.AXScriptAttribute): ...
class NamedScriptAttribute(pyscript.NamedScriptAttribute): ...
class PyScript(pyscript.PyScript): ...

def Register() -> None: ...
