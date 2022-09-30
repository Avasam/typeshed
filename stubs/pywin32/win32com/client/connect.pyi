from _typeshed import Incomplete

class SimpleConnection:
    cp: Incomplete
    cookie: Incomplete
    debug: Incomplete
    def __init__(
        self,
        coInstance: Incomplete | None = ...,
        eventInstance: Incomplete | None = ...,
        eventCLSID: Incomplete | None = ...,
        debug: int = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def Connect(self, coInstance, eventInstance, eventCLSID: Incomplete | None = ...) -> None: ...
    def Disconnect(self) -> None: ...
