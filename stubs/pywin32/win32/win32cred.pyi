from typing import Any

CREDUI_FLAGS_ALWAYS_SHOW_UI: int
CREDUI_FLAGS_COMPLETE_USERNAME: int
CREDUI_FLAGS_DO_NOT_PERSIST: int
CREDUI_FLAGS_EXCLUDE_CERTIFICATES: int
CREDUI_FLAGS_EXPECT_CONFIRMATION: int
CREDUI_FLAGS_GENERIC_CREDENTIALS: int
CREDUI_FLAGS_INCORRECT_PASSWORD: int
CREDUI_FLAGS_KEEP_USERNAME: int
CREDUI_FLAGS_PASSWORD_ONLY_OK: int
CREDUI_FLAGS_PERSIST: int
CREDUI_FLAGS_PROMPT_VALID: int
CREDUI_FLAGS_REQUEST_ADMINISTRATOR: int
CREDUI_FLAGS_REQUIRE_CERTIFICATE: int
CREDUI_FLAGS_REQUIRE_SMARTCARD: int
CREDUI_FLAGS_SERVER_CREDENTIAL: int
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX: int
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS: int
CREDUI_FLAGS_VALIDATE_USERNAME: int
CREDUI_MAX_CAPTION_LENGTH: int
CREDUI_MAX_DOMAIN_TARGET_LENGTH: int
CREDUI_MAX_GENERIC_TARGET_LENGTH: int
CREDUI_MAX_MESSAGE_LENGTH: int
CREDUI_MAX_PASSWORD_LENGTH: int
CREDUI_MAX_USERNAME_LENGTH: int
CRED_ALLOW_NAME_RESOLUTION: int
CRED_CACHE_TARGET_INFORMATION: int
CRED_FLAGS_OWF_CRED_BLOB: int
CRED_FLAGS_PASSWORD_FOR_CERT: int
CRED_FLAGS_PROMPT_NOW: int
CRED_FLAGS_USERNAME_TARGET: int
CRED_FLAGS_VALID_FLAGS: int
CRED_MAX_ATTRIBUTES: int
CRED_MAX_DOMAIN_TARGET_NAME_LENGTH: int
CRED_MAX_GENERIC_TARGET_NAME_LENGTH: int
CRED_MAX_STRING_LENGTH: int
CRED_MAX_USERNAME_LENGTH: int
CRED_MAX_VALUE_SIZE: int
CRED_PERSIST_ENTERPRISE: int
CRED_PERSIST_LOCAL_MACHINE: int
CRED_PERSIST_NONE: int
CRED_PERSIST_SESSION: int
CRED_PRESERVE_CREDENTIAL_BLOB: int
CRED_TI_CREATE_EXPLICIT_CRED: int
CRED_TI_DOMAIN_FORMAT_UNKNOWN: int
CRED_TI_ONLY_PASSWORD_REQUIRED: int
CRED_TI_SERVER_FORMAT_UNKNOWN: int
CRED_TI_USERNAME_TARGET: int
CRED_TI_VALID_FLAGS: int
CRED_TI_WORKGROUP_MEMBER: int
CRED_TYPE_DOMAIN_CERTIFICATE: int
CRED_TYPE_DOMAIN_PASSWORD: int
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD: int
CRED_TYPE_GENERIC: int
CertCredential: int
UsernameTargetCredential: int

def CredDelete(*args, **kwargs) -> Any: ...
def CredEnumerate(*args, **kwargs) -> Any: ...
def CredGetTargetInfo(*args, **kwargs) -> Any: ...
def CredIsMarshaledCredential(*args, **kwargs) -> Any: ...
def CredMarshalCredential(*args, **kwargs) -> Any: ...
def CredRead(*args, **kwargs) -> Any: ...
def CredReadDomainCredentials(*args, **kwargs) -> Any: ...
def CredRename(*args, **kwargs) -> Any: ...
def CredUICmdLinePromptForCredentials(*args, **kwargs) -> Any: ...
def CredUIConfirmCredentials(*args, **kwargs) -> Any: ...
def CredUIParseUserName(*args, **kwargs) -> Any: ...
def CredUIPromptForCredentials(*args, **kwargs) -> Any: ...
def CredUIReadSSOCredW(*args, **kwargs) -> Any: ...
def CredUIStoreSSOCredW(*args, **kwargs) -> Any: ...
def CredUnmarshalCredential(*args, **kwargs) -> Any: ...
def CredWrite(*args, **kwargs) -> Any: ...
def CredWriteDomainCredentials(*args, **kwargs) -> Any: ...
