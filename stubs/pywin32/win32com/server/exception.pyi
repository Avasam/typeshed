from _typeshed import Incomplete

# import pythoncom # Crashes stubtest
pythoncom: Incomplete

class COMException(pythoncom.com_error):  # noqa: F821
    scode: Incomplete
    description: Incomplete
    source: Incomplete
    helpfile: Incomplete
    helpcontext: Incomplete
    def __init__(
        self,
        description: Incomplete | None = ...,
        scode: Incomplete | None = ...,
        source: Incomplete | None = ...,
        helpfile: Incomplete | None = ...,
        helpContext: Incomplete | None = ...,
        desc: Incomplete | None = ...,
        hresult: Incomplete | None = ...,
    ) -> None: ...

Exception = COMException

def IsCOMException(t: Incomplete | None = ...): ...
def IsCOMServerException(t: Incomplete | None = ...): ...
