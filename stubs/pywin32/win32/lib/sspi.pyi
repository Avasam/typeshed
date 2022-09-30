from _typeshed import Incomplete

error: Incomplete

class _BaseAuth:
    def __init__(self) -> None: ...
    ctxt: Incomplete
    authenticated: bool
    initiator_name: Incomplete
    service_name: Incomplete
    next_seq_num: int
    def reset(self) -> None: ...
    def encrypt(self, data): ...
    def decrypt(self, data, trailer): ...
    def sign(self, data): ...
    def verify(self, data, sig) -> None: ...
    def unwrap(self, token): ...
    def wrap(self, msg, encrypt: bool = ...): ...

class ClientAuth(_BaseAuth):
    scflags: Incomplete
    datarep: Incomplete
    targetspn: Incomplete
    pkg_info: Incomplete
    def __init__(
        self,
        pkg_name,
        client_name: Incomplete | None = ...,
        auth_info: Incomplete | None = ...,
        targetspn: Incomplete | None = ...,
        scflags: Incomplete | None = ...,
        datarep=...,
    ) -> None: ...
    ctxt: Incomplete
    ctxt_attr: Incomplete
    ctxt_expiry: Incomplete
    authenticated: Incomplete
    def authorize(self, sec_buffer_in): ...

class ServerAuth(_BaseAuth):
    spn: Incomplete
    datarep: Incomplete
    scflags: Incomplete
    pkg_info: Incomplete
    def __init__(self, pkg_name, spn: Incomplete | None = ..., scflags: Incomplete | None = ..., datarep=...) -> None: ...
    ctxt: Incomplete
    ctxt_attr: Incomplete
    ctxt_expiry: Incomplete
    authenticated: Incomplete
    def authorize(self, sec_buffer_in): ...
