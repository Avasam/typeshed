from logging import Logger

from oauthlib.oauth2.rfc6749.request_validator import RequestValidator as OAuth2RequestValidator

log: Logger

class RequestValidator(OAuth2RequestValidator):
    def get_authorization_code_scopes(self, client_id, code, redirect_uri, request) -> None: ...
    def get_authorization_code_nonce(self, client_id, code, redirect_uri, request) -> None: ...
    def get_jwt_bearer_token(self, token, token_handler, request) -> None: ...
    def get_id_token(self, token, token_handler, request) -> None: ...
    def finalize_id_token(self, id_token, token, token_handler, request) -> None: ...
    def validate_jwt_bearer_token(self, token, scopes, request) -> None: ...
    def validate_id_token(self, token, scopes, request) -> None: ...
    def validate_silent_authorization(self, request) -> None: ...
    def validate_silent_login(self, request) -> None: ...
    def validate_user_match(self, id_token_hint, scopes, claims, request) -> None: ...
    def get_userinfo_claims(self, request) -> None: ...
