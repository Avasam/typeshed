from typing import Any

class OAuth2Token(dict):
    def __init__(self, params, old_scope: Any | None = ...) -> None: ...
    @property
    def scope_changed(self): ...
    @property
    def old_scope(self): ...
    @property
    def old_scopes(self): ...
    @property
    def scope(self): ...
    @property
    def scopes(self): ...
    @property
    def missing_scopes(self): ...
    @property
    def additional_scopes(self): ...

def prepare_mac_header(
    token,
    uri,
    key,
    http_method,
    nonce: Any | None = ...,
    headers: Any | None = ...,
    body: Any | None = ...,
    ext: str = ...,
    hash_algorithm: str = ...,
    issue_time: Any | None = ...,
    draft: int = ...,
): ...
def prepare_bearer_uri(token, uri): ...
def prepare_bearer_headers(token, headers: Any | None = ...): ...
def prepare_bearer_body(token, body: str = ...): ...
def random_token_generator(request, refresh_token: bool = ...): ...
def signed_token_generator(private_pem, **kwargs): ...
def get_token_from_header(request): ...

class TokenBase:
    def __call__(self, request, refresh_token: bool = ...) -> None: ...
    def validate_request(self, request) -> None: ...
    def estimate_type(self, request) -> None: ...

class BearerToken(TokenBase):
    request_validator: Any
    token_generator: Any
    refresh_token_generator: Any
    expires_in: Any
    def __init__(
        self,
        request_validator: Any | None = ...,
        token_generator: Any | None = ...,
        expires_in: Any | None = ...,
        refresh_token_generator: Any | None = ...,
    ) -> None: ...
    def create_token(self, request, refresh_token: bool = ..., **kwargs): ...
    def validate_request(self, request): ...
    def estimate_type(self, request): ...
