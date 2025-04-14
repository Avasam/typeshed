from _typeshed import Incomplete

from .. import TokenValidationError as TokenValidationError
from ..rest_async import AsyncRestClient as AsyncRestClient
from .token_verifier import (
    AsymmetricSignatureVerifier as AsymmetricSignatureVerifier,
    JwksFetcher as JwksFetcher,
    TokenVerifier as TokenVerifier,
)

class AsyncAsymmetricSignatureVerifier(AsymmetricSignatureVerifier):
    def __init__(self, jwks_url: str, algorithm: str = "RS256") -> None: ...
    def set_session(self, session) -> None: ...
    async def verify_signature(self, token) -> dict[str, Incomplete]: ...  # type: ignore[override] # Differs from supertype

class AsyncJwksFetcher(JwksFetcher):
    def __init__(self, *args, **kwargs) -> None: ...
    def set_session(self, session) -> None: ...
    async def get_key(self, key_id: str): ...

class AsyncTokenVerifier(TokenVerifier):
    iss: str
    aud: str
    leeway: int
    def __init__(
        self, signature_verifier: AsyncAsymmetricSignatureVerifier, issuer: str, audience: str, leeway: int = 0
    ) -> None: ...
    def set_session(self, session) -> None: ...
    async def verify(  # type: ignore[override] # Differs from supertype
        self, token: str, nonce: str | None = None, max_age: int | None = None, organization: str | None = None
    ) -> dict[str, Incomplete]: ...
