import _win32typing
from win32com.client.dynamic import CDispatch, _GoodDispatchTypes

def EnsureDispatch(
    prog_id: str | _win32typing.PyIDispatch | _GoodDispatchTypes | _win32typing.PyIUnknown, bForDemand: int = ...
) -> CDispatch: ...
