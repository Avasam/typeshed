from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import TypeAlias

import _win32typing
from win32.lib.pywintypes import (
    ACLType,
    HANDLEType,
    IIDType,
    SECURITY_ATTRIBUTESType,
    SECURITY_DESCRIPTORType,
    SIDType,
    TimeType,
    error as error,
)

def DsGetSpn(
    ServiceType,
    ServiceClass: str,
    ServiceName: str,
    InstancePort: int = ...,
    InstanceNames: tuple[str, ...] | None = ...,
    InstancePorts: tuple[Incomplete, ...] | None = ...,
    /,
) -> tuple[str, ...]: ...
def DsWriteAccountSpn(hDS: _win32typing.PyDS_HANDLE, Operation, Account: str, Spns: tuple[str, ...], /) -> None: ...
def DsBind(DomainController: str, DnsDomainName: str, /) -> _win32typing.PyDS_HANDLE: ...
def DsUnBind(hDS: _win32typing.PyDS_HANDLE, /) -> None: ...
def DsGetDcName(
    computerName: str | None = ...,
    domainName: str | None = ...,
    domainGUID: IIDType | None = ...,
    siteName: str | None = ...,
    flags: int = ...,
): ...
def DsCrackNames(
    hds: _win32typing.PyDS_HANDLE, flags, formatOffered, formatDesired, names: list[Incomplete], /
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def ACL(bufSize: int = ..., /) -> ACLType: ...
def SID() -> SIDType: ...
def SECURITY_ATTRIBUTES() -> SECURITY_ATTRIBUTESType: ...
def SECURITY_DESCRIPTOR() -> SECURITY_DESCRIPTORType: ...
def ImpersonateNamedPipeClient(handle, /) -> None: ...
def ImpersonateLoggedOnUser(handle: int, /) -> None: ...
def ImpersonateAnonymousToken(ThreadHandle: int, /) -> None: ...
def IsTokenRestricted(TokenHandle: int | None, /) -> bool: ...
def RevertToSelf() -> None: ...
def LogonUser(Username: str, Domain: str | None, Password: str, LogonType: int, LogonProvider: int) -> HANDLEType: ...
def LogonUserEx(
    Username: str, Domain: str, Password: str, LogonType, LogonProvider
) -> tuple[int, SIDType, Incomplete, Incomplete]: ...
def LookupAccountName(systemName: str | None, accountName: str, /) -> tuple[SIDType, str, int]: ...
def LookupAccountSid(systemName: str, sid: SIDType, /) -> tuple[str, str, Incomplete]: ...
def GetBinarySid(SID: str, /) -> SIDType: ...
def SetSecurityInfo(
    handle: int, ObjectType, SecurityInfo, Owner: SIDType, Group: SIDType, Dacl: ACLType, Sacl: ACLType, /
) -> None: ...
def GetSecurityInfo(handle: int, ObjectType, SecurityInfo, /) -> SECURITY_DESCRIPTORType: ...
def SetNamedSecurityInfo(
    ObjectName: str,
    ObjectType: int,
    SecurityInfo: int,
    Owner: SIDType | None,
    Group: SIDType | None,
    Dacl: ACLType | None,
    Sacl: ACLType | None,
    /,
) -> None: ...
def GetNamedSecurityInfo(ObjectName: str, ObjectType: int, SecurityInfo: int, /) -> SECURITY_DESCRIPTORType: ...
def OpenProcessToken(processHandle, desiredAccess, /) -> int: ...
def LookupPrivilegeValue(systemName: str, privilegeName: str, /) -> _win32typing.LARGE_INTEGER: ...
def LookupPrivilegeName(SystemName: str, luid: _win32typing.LARGE_INTEGER, /) -> str: ...
def LookupPrivilegeDisplayName(SystemName: str, Name: str, /) -> str: ...
def AdjustTokenPrivileges(
    TokenHandle: int, bDisableAllPrivileges, NewState: _win32typing.PyTOKEN_PRIVILEGES
) -> _win32typing.PyTOKEN_PRIVILEGES: ...
def AdjustTokenGroups(TokenHandle: int, ResetToDefault, NewState: _win32typing.PyTOKEN_GROUPS) -> _win32typing.PyTOKEN_GROUPS: ...
def GetTokenInformation(TokenHandle: int, TokenInformationClass, /): ...
def OpenThreadToken(handle: int, desiredAccess, openAsSelf, /): ...
def SetThreadToken(Thread: int, Token: int, /) -> None: ...
def GetFileSecurity(filename: str, info: int = ..., /) -> SECURITY_DESCRIPTORType: ...
def SetFileSecurity(filename: str, info: int, security: SECURITY_DESCRIPTORType, /) -> None: ...
def GetUserObjectSecurity(handle: int, info, /) -> SECURITY_DESCRIPTORType: ...
def SetUserObjectSecurity(handle: int, info, security: SECURITY_DESCRIPTORType, /) -> None: ...
def GetKernelObjectSecurity(handle: int, info, /) -> SECURITY_DESCRIPTORType: ...
def SetKernelObjectSecurity(handle: int, info, security: SECURITY_DESCRIPTORType, /) -> None: ...
def SetTokenInformation(TokenHandle: int, TokenInformationClass, TokenInformation, /) -> None: ...
def LsaOpenPolicy(system_name: str, access_mask, /) -> _win32typing.PyLSA_HANDLE: ...
def LsaClose(PolicyHandle: int, /) -> None: ...
def LsaQueryInformationPolicy(PolicyHandle: _win32typing.PyLSA_HANDLE, InformationClass, /) -> None: ...
def LsaSetInformationPolicy(PolicyHandle: _win32typing.PyLSA_HANDLE, InformationClass, Information, /) -> None: ...
def LsaAddAccountRights(
    PolicyHandle: _win32typing.PyLSA_HANDLE, AccountSid: SIDType, UserRights: tuple[Incomplete, ...]
) -> None: ...
def LsaRemoveAccountRights(
    PolicyHandle: _win32typing.PyLSA_HANDLE, AccountSid: SIDType, AllRights, UserRights: tuple[Incomplete, ...]
) -> None: ...
def LsaEnumerateAccountRights(PolicyHandle: _win32typing.PyLSA_HANDLE, AccountSid: SIDType, /) -> list[str]: ...
def LsaEnumerateAccountsWithUserRight(PolicyHandle: _win32typing.PyLSA_HANDLE, UserRight, /) -> tuple[SIDType, ...]: ...
def ConvertSidToStringSid(Sid: SIDType, /) -> str: ...
def ConvertStringSidToSid(StringSid: str, /) -> SIDType: ...
def ConvertSecurityDescriptorToStringSecurityDescriptor(
    SecurityDescriptor: SECURITY_DESCRIPTORType, RequestedStringSDRevision, SecurityInformation, /
) -> str: ...
def ConvertStringSecurityDescriptorToSecurityDescriptor(
    StringSecurityDescriptor: str, StringSDRevision, /
) -> SECURITY_DESCRIPTORType: ...
def LsaStorePrivateData(PolicyHandle: _win32typing.PyLSA_HANDLE, KeyName: str, PrivateData, /) -> None: ...
def LsaRetrievePrivateData(PolicyHandle: _win32typing.PyLSA_HANDLE, KeyName: str, /) -> str: ...
def LsaRegisterPolicyChangeNotification(InformationClass, NotificationEventHandle: int, /) -> None: ...
def LsaUnregisterPolicyChangeNotification(InformationClass, NotificationEventHandle: int, /) -> None: ...
def CryptEnumProviders() -> list[tuple[str, Incomplete]]: ...
def EnumerateSecurityPackages() -> tuple[Incomplete, ...]: ...
def AllocateLocallyUniqueId() -> None: ...
def ImpersonateSelf(ImpersonationLevel, /) -> None: ...
def DuplicateToken(ExistingTokenHandle: int, ImpersonationLevel, /) -> int: ...
def DuplicateTokenEx(
    ExistingToken: int, ImpersonationLevel, DesiredAccess, TokenType, TokenAttributes: SECURITY_ATTRIBUTESType | None = ...
) -> int: ...
def CheckTokenMembership(TokenHandle: int, SidToCheck: SIDType, /): ...
def CreateRestrictedToken(
    ExistingTokenHandle: int,
    Flags,
    SidsToDisable: tuple[_win32typing.PySID_AND_ATTRIBUTES, ...],
    PrivilegesToDelete: tuple[_win32typing.PyLUID_AND_ATTRIBUTES, ...],
    SidsToRestrict: tuple[_win32typing.PySID_AND_ATTRIBUTES, ...],
) -> int: ...
def LsaRegisterLogonProcess(LogonProcessName: str, /) -> _win32typing.PyLsaLogon_HANDLE: ...
def LsaConnectUntrusted() -> _win32typing.PyLsaLogon_HANDLE: ...
def LsaDeregisterLogonProcess(LsaHandle: _win32typing.PyLsaLogon_HANDLE, /) -> None: ...
def LsaLookupAuthenticationPackage(LsaHandle: _win32typing.PyLsaLogon_HANDLE, PackageName: str, /): ...
def LsaEnumerateLogonSessions() -> tuple[Incomplete, ...]: ...
def LsaGetLogonSessionData(LogonId, /) -> tuple[Incomplete, ...]: ...
def AcquireCredentialsHandle(Principal, Package, CredentialUse, LogonID, AuthData, /) -> tuple[PyCredHandleType, TimeType]: ...
def InitializeSecurityContext(
    Credential: PyCredHandleType,
    Context: PyCtxtHandleType,
    TargetName,
    ContextReq,
    TargetDataRep,
    pInput: PySecBufferDescType,
    NewContext: PyCtxtHandleType,
    pOutput: PySecBufferDescType,
    /,
) -> tuple[Incomplete, Incomplete, TimeType]: ...
def AcceptSecurityContext(
    Credential: PyCredHandleType,
    Context: PyCtxtHandleType,
    pInput: PySecBufferDescType,
    ContextReq,
    TargetDataRep,
    NewContext: PyCtxtHandleType,
    pOutput: PySecBufferDescType,
    /,
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def QuerySecurityPackageInfo(PackageName, /): ...
def LsaCallAuthenticationPackage(
    LsaHandle: _win32typing.PyLsaLogon_HANDLE, AuthenticationPackage, MessageType, ProtocolSubmitBuffer, /
) -> None: ...
def TranslateName(accountName: str, accountNameFormat, accountNameFormat1, numChars=..., /) -> str: ...
def CreateWellKnownSid(WellKnownSidType, DomainSid: SIDType | None = ..., /) -> SIDType: ...
def MapGenericMask(AccessMask, GenericMapping: tuple[Incomplete, Incomplete, Incomplete, Incomplete], /): ...

class PySecBufferType:
    __name__: ClassVar[str] = "PySecBuffer"
    def __init__(self, BufferSize, BufferType) -> None: ...
    @property
    def BufferType(self): ...
    @property
    def Buffer(self) -> str: ...
    @property
    def BufferSize(self): ...
    @property
    def MaxBufferSize(self): ...
    def Clear(self) -> None: ...

class PySecBufferDescType:
    __name__: ClassVar[str] = "PySecBufferDesc"
    def __init__(self, Version=...) -> None: ...
    Version: Incomplete
    Buffer: Incomplete
    def append(self, buffer, /) -> None: ...

class PyCtxtHandleType:
    __name__: ClassVar[str] = "PyCtxtHandle"
    def Detach(self): ...
    def CompleteAuthToken(self, Token: PySecBufferDescType, /) -> None: ...
    def QueryContextAttributes(self, Attribute, /) -> None: ...
    def DeleteSecurityContext(self) -> None: ...
    def QuerySecurityContextToken(self): ...
    def MakeSignature(self, fqop, Message: PySecBufferDescType, MessageSeqNo, /) -> None: ...
    def VerifySignature(self, Message: PySecBufferDescType, MessageSeqNo, /) -> None: ...
    def EncryptMessage(self, fqop, Message: PySecBufferDescType, MessageSeqNo, /) -> None: ...
    def DecryptMessage(self, Message: PySecBufferDescType, MessageSeqNo, /) -> None: ...
    def ImpersonateSecurityContext(self) -> None: ...
    def RevertSecurityContext(self) -> None: ...

class PyCredHandleType:
    __name__: ClassVar[str] = "PyCredHandle"
    def Detach(self): ...
    def FreeCredentialsHandle(self) -> None: ...
    def QueryCredentialsAttributes(self, Attribute, /) -> None: ...

# old names, these should not be used
SecBufferType: TypeAlias = PySecBufferType
SecBufferDescType: TypeAlias = PySecBufferDescType
CtxtHandleType: TypeAlias = PyCtxtHandleType
CredHandleType: TypeAlias = PyCredHandleType

ACCESS_ALLOWED_ACE_TYPE: int
ACCESS_ALLOWED_OBJECT_ACE_TYPE: int
ACCESS_DENIED_ACE_TYPE: int
ACCESS_DENIED_OBJECT_ACE_TYPE: int
ACL_REVISION: int
ACL_REVISION_DS: int
AuditCategoryAccountLogon: int
AuditCategoryAccountManagement: int
AuditCategoryDetailedTracking: int
AuditCategoryDirectoryServiceAccess: int
AuditCategoryLogon: int
AuditCategoryObjectAccess: int
AuditCategoryPolicyChange: int
AuditCategoryPrivilegeUse: int
AuditCategorySystem: int
CONTAINER_INHERIT_ACE: int
DACL_SECURITY_INFORMATION: int
DENY_ACCESS: int
DISABLE_MAX_PRIVILEGE: int
DS_SPN_ADD_SPN_OP: int
DS_SPN_DELETE_SPN_OP: int
DS_SPN_DN_HOST: int
DS_SPN_DNS_HOST: int
DS_SPN_DOMAIN: int
DS_SPN_NB_DOMAIN: int
DS_SPN_NB_HOST: int
DS_SPN_REPLACE_SPN_OP: int
DS_SPN_SERVICE: int
FAILED_ACCESS_ACE_FLAG: int
GRANT_ACCESS: int
GROUP_SECURITY_INFORMATION: int
INHERIT_ONLY_ACE: int
INHERITED_ACE: int
LABEL_SECURITY_INFORMATION: int
LOGON32_LOGON_BATCH: int
LOGON32_LOGON_INTERACTIVE: int
LOGON32_LOGON_NETWORK: int
LOGON32_LOGON_NETWORK_CLEARTEXT: int
LOGON32_LOGON_NEW_CREDENTIALS: int
LOGON32_LOGON_SERVICE: int
LOGON32_LOGON_UNLOCK: int
LOGON32_PROVIDER_DEFAULT: int
LOGON32_PROVIDER_WINNT35: int
LOGON32_PROVIDER_WINNT40: int
LOGON32_PROVIDER_WINNT50: int
NO_INHERITANCE: int
NO_PROPAGATE_INHERIT_ACE: int
NOT_USED_ACCESS: int
OBJECT_INHERIT_ACE: int
OWNER_SECURITY_INFORMATION: int
POLICY_ALL_ACCESS: int
POLICY_AUDIT_EVENT_FAILURE: int
POLICY_AUDIT_EVENT_NONE: int
POLICY_AUDIT_EVENT_SUCCESS: int
POLICY_AUDIT_EVENT_UNCHANGED: int
POLICY_AUDIT_LOG_ADMIN: int
POLICY_CREATE_ACCOUNT: int
POLICY_CREATE_PRIVILEGE: int
POLICY_CREATE_SECRET: int
POLICY_EXECUTE: int
POLICY_GET_PRIVATE_INFORMATION: int
POLICY_LOOKUP_NAMES: int
POLICY_NOTIFICATION: int
POLICY_READ: int
POLICY_SERVER_ADMIN: int
POLICY_SET_AUDIT_REQUIREMENTS: int
POLICY_SET_DEFAULT_QUOTA_LIMITS: int
POLICY_TRUST_ADMIN: int
POLICY_VIEW_AUDIT_INFORMATION: int
POLICY_VIEW_LOCAL_INFORMATION: int
POLICY_WRITE: int
PolicyAccountDomainInformation: int
PolicyAuditEventsInformation: int
PolicyAuditFullQueryInformation: int
PolicyAuditFullSetInformation: int
PolicyAuditLogInformation: int
PolicyDefaultQuotaInformation: int
PolicyDnsDomainInformation: int
PolicyLsaServerRoleInformation: int
PolicyModificationInformation: int
PolicyNotifyAccountDomainInformation: int
PolicyNotifyAuditEventsInformation: int
PolicyNotifyDnsDomainInformation: int
PolicyNotifyDomainEfsInformation: int
PolicyNotifyDomainKerberosTicketInformation: int
PolicyNotifyMachineAccountPasswordInformation: int
PolicyNotifyServerRoleInformation: int
PolicyPdAccountInformation: int
PolicyPrimaryDomainInformation: int
PolicyReplicaSourceInformation: int
PolicyServerDisabled: int
PolicyServerEnabled: int
PolicyServerRoleBackup: int
PolicyServerRolePrimary: int
PROTECTED_DACL_SECURITY_INFORMATION: int
PROTECTED_SACL_SECURITY_INFORMATION: int
REVOKE_ACCESS: int
SACL_SECURITY_INFORMATION: int
SANDBOX_INERT: int
SDDL_REVISION_1: int
SE_DACL_AUTO_INHERITED: int
SE_DACL_DEFAULTED: int
SE_DACL_PRESENT: int
SE_DACL_PROTECTED: int
SE_DS_OBJECT: int
SE_DS_OBJECT_ALL: int
SE_FILE_OBJECT: int
SE_GROUP_DEFAULTED: int
SE_GROUP_ENABLED: int
SE_GROUP_ENABLED_BY_DEFAULT: int
SE_GROUP_LOGON_ID: int
SE_GROUP_MANDATORY: int
SE_GROUP_OWNER: int
SE_GROUP_RESOURCE: int
SE_GROUP_USE_FOR_DENY_ONLY: int
SE_KERNEL_OBJECT: int
SE_LMSHARE: int
SE_OWNER_DEFAULTED: int
SE_PRINTER: int
SE_PRIVILEGE_ENABLED: int
SE_PRIVILEGE_ENABLED_BY_DEFAULT: int
SE_PRIVILEGE_REMOVED: int
SE_PRIVILEGE_USED_FOR_ACCESS: int
SE_PROVIDER_DEFINED_OBJECT: int
SE_REGISTRY_KEY: int
SE_REGISTRY_WOW64_32KEY: int
SE_SACL_AUTO_INHERITED: int
SE_SACL_DEFAULTED: int
SE_SACL_PRESENT: int
SE_SACL_PROTECTED: int
SE_SELF_RELATIVE: int
SE_SERVICE: int
SE_UNKNOWN_OBJECT_TYPE: int
SE_WINDOW_OBJECT: int
SE_WMIGUID_OBJECT: int
SECPKG_CRED_BOTH: int
SECPKG_CRED_INBOUND: int
SECPKG_CRED_OUTBOUND: int
SECPKG_FLAG_ACCEPT_WIN32_NAME: int
SECPKG_FLAG_CLIENT_ONLY: int
SECPKG_FLAG_CONNECTION: int
SECPKG_FLAG_DATAGRAM: int
SECPKG_FLAG_EXTENDED_ERROR: int
SECPKG_FLAG_IMPERSONATION: int
SECPKG_FLAG_INTEGRITY: int
SECPKG_FLAG_MULTI_REQUIRED: int
SECPKG_FLAG_PRIVACY: int
SECPKG_FLAG_STREAM: int
SECPKG_FLAG_TOKEN_ONLY: int
SECURITY_CREATOR_SID_AUTHORITY: int
SECURITY_LOCAL_SID_AUTHORITY: int
SECURITY_NON_UNIQUE_AUTHORITY: int
SECURITY_NT_AUTHORITY: int
SECURITY_NULL_SID_AUTHORITY: int
SECURITY_RESOURCE_MANAGER_AUTHORITY: int
SECURITY_WORLD_SID_AUTHORITY: int
SecurityAnonymous: int
SecurityDelegation: int
SecurityIdentification: int
SecurityImpersonation: int
SET_ACCESS: int
SET_AUDIT_FAILURE: int
SET_AUDIT_SUCCESS: int
SidTypeAlias: int
SidTypeComputer: int
SidTypeDeletedAccount: int
SidTypeDomain: int
SidTypeGroup: int
SidTypeInvalid: int
SidTypeUnknown: int
SidTypeUser: int
SidTypeWellKnownGroup: int
STYPE_DEVICE: int
STYPE_DISKTREE: int
STYPE_IPC: int
STYPE_PRINTQ: int
STYPE_SPECIAL: int
STYPE_TEMPORARY: int
SUB_CONTAINERS_AND_OBJECTS_INHERIT: int
SUB_CONTAINERS_ONLY_INHERIT: int
SUB_OBJECTS_ONLY_INHERIT: int
SUCCESSFUL_ACCESS_ACE_FLAG: int
SYSTEM_AUDIT_ACE_TYPE: int
SYSTEM_AUDIT_OBJECT_ACE_TYPE: int
TOKEN_ADJUST_DEFAULT: int
TOKEN_ADJUST_GROUPS: int
TOKEN_ADJUST_PRIVILEGES: int
TOKEN_ALL_ACCESS: int
TOKEN_ASSIGN_PRIMARY: int
TOKEN_DUPLICATE: int
TOKEN_EXECUTE: int
TOKEN_IMPERSONATE: int
TOKEN_QUERY: int
TOKEN_QUERY_SOURCE: int
TOKEN_READ: int
TOKEN_WRITE: int
TokenImpersonation: int
TokenPrimary: int
TrustedControllersInformation: int
TrustedDomainAuthInformation: int
TrustedDomainAuthInformationInternal: int
TrustedDomainFullInformation: int
TrustedDomainFullInformation2Internal: int
TrustedDomainFullInformationInternal: int
TrustedDomainInformationBasic: int
TrustedDomainInformationEx: int
TrustedDomainInformationEx2Internal: int
TrustedDomainNameInformation: int
TrustedPasswordInformation: int
TrustedPosixOffsetInformation: int
TRUSTEE_BAD_FORM: int
TRUSTEE_IS_ALIAS: int
TRUSTEE_IS_COMPUTER: int
TRUSTEE_IS_DELETED: int
TRUSTEE_IS_DOMAIN: int
TRUSTEE_IS_GROUP: int
TRUSTEE_IS_INVALID: int
TRUSTEE_IS_NAME: int
TRUSTEE_IS_OBJECTS_AND_NAME: int
TRUSTEE_IS_OBJECTS_AND_SID: int
TRUSTEE_IS_SID: int
TRUSTEE_IS_UNKNOWN: int
TRUSTEE_IS_USER: int
TRUSTEE_IS_WELL_KNOWN_GROUP: int
UNPROTECTED_DACL_SECURITY_INFORMATION: int
UNPROTECTED_SACL_SECURITY_INFORMATION: int

def DsListDomainsInSite(*args): ...  # incomplete
def DsListInfoForServer(*args): ...  # incomplete
def DsListRoles(*args): ...  # incomplete
def DsListServersForDomainInSite(*args): ...  # incomplete
def DsListServersInSite(*args): ...  # incomplete
def DsListSites(*args): ...  # incomplete
def GetPolicyHandle(*args): ...  # incomplete

MICROSOFT_KERBEROS_NAME_A: bytes
MSV1_0_PACKAGE_NAME: bytes
SE_ASSIGNPRIMARYTOKEN_NAME: str
SE_AUDIT_NAME: str
SE_BACKUP_NAME: str
SE_BATCH_LOGON_NAME: str
SE_CHANGE_NOTIFY_NAME: str
SE_CREATE_GLOBAL_NAME: str
SE_CREATE_PAGEFILE_NAME: str
SE_CREATE_PERMANENT_NAME: str
SE_CREATE_SYMBOLIC_LINK_NAME: str
SE_CREATE_TOKEN_NAME: str
SE_DEBUG_NAME: str
SE_DENY_BATCH_LOGON_NAME: str
SE_DENY_INTERACTIVE_LOGON_NAME: str
SE_DENY_NETWORK_LOGON_NAME: str
SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_DENY_SERVICE_LOGON_NAME: str
SE_ENABLE_DELEGATION_NAME: str
SE_GROUP_INTEGRITY: int
SE_GROUP_INTEGRITY_ENABLED: int
SE_IMPERSONATE_NAME: str
SE_INCREASE_QUOTA_NAME: str
SE_INC_BASE_PRIORITY_NAME: str
SE_INC_WORKING_SET_NAME: str
SE_INTERACTIVE_LOGON_NAME: str
SE_LOAD_DRIVER_NAME: str
SE_LOCK_MEMORY_NAME: str
SE_MACHINE_ACCOUNT_NAME: str
SE_MANAGE_VOLUME_NAME: str
SE_NETWORK_LOGON_NAME: str
SE_PROF_SINGLE_PROCESS_NAME: str
SE_RELABEL_NAME: str
SE_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_REMOTE_SHUTDOWN_NAME: str
SE_RESTORE_NAME: str
SE_SECURITY_NAME: str
SE_SERVICE_LOGON_NAME: str
SE_SHUTDOWN_NAME: str
SE_SYNC_AGENT_NAME: str
SE_SYSTEMTIME_NAME: str
SE_SYSTEM_ENVIRONMENT_NAME: str
SE_SYSTEM_PROFILE_NAME: str
SE_TAKE_OWNERSHIP_NAME: str
SE_TCB_NAME: str
SE_TIME_ZONE_NAME: str
SE_TRUSTED_CREDMAN_ACCESS_NAME: str
SE_UNDOCK_NAME: str
SE_UNSOLICITED_INPUT_NAME: str
SYSTEM_MANDATORY_LABEL_NO_EXECUTE_UP: int
SYSTEM_MANDATORY_LABEL_NO_READ_UP: int
SYSTEM_MANDATORY_LABEL_NO_WRITE_UP: int
SYSTEM_MANDATORY_LABEL_VALID_MASK: int
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN: int
TOKEN_MANDATORY_POLICY_NO_WRITE_UP: int
TOKEN_MANDATORY_POLICY_OFF: int
TOKEN_MANDATORY_POLICY_VALID_MASK: int
TokenAccessInformation: int
TokenAuditPolicy: int
TokenDefaultDacl: int
TokenElevation: int
TokenElevationType: int
TokenElevationTypeDefault: int
TokenElevationTypeFull: int
TokenElevationTypeLimited: int
TokenGroups: int
TokenGroupsAndPrivileges: int
TokenHasRestrictions: int
TokenImpersonationLevel: int
TokenIntegrityLevel: int
TokenLinkedToken: int
TokenLogonSid: int
TokenMandatoryPolicy: int
TokenOrigin: int
TokenOwner: int
TokenPrimaryGroup: int
TokenPrivileges: int
TokenRestrictedSids: int
TokenSandBoxInert: int
TokenSessionId: int
TokenSessionReference: int
TokenSource: int
TokenStatistics: int
TokenType: int
TokenUIAccess: int
TokenUser: int
TokenVirtualizationAllowed: int
TokenVirtualizationEnabled: int
UNICODE: int
WinAccountAdministratorSid: int
WinAccountCertAdminsSid: int
WinAccountComputersSid: int
WinAccountControllersSid: int
WinAccountDomainAdminsSid: int
WinAccountDomainGuestsSid: int
WinAccountDomainUsersSid: int
WinAccountEnterpriseAdminsSid: int
WinAccountGuestSid: int
WinAccountKrbtgtSid: int
WinAccountPolicyAdminsSid: int
WinAccountRasAndIasServersSid: int
WinAccountReadonlyControllersSid: int
WinAccountSchemaAdminsSid: int
WinAnonymousSid: int
WinAuthenticatedUserSid: int
WinBatchSid: int
WinBuiltinAccountOperatorsSid: int
WinBuiltinAdministratorsSid: int
WinBuiltinAuthorizationAccessSid: int
WinBuiltinBackupOperatorsSid: int
WinBuiltinCryptoOperatorsSid: int
WinBuiltinDCOMUsersSid: int
WinBuiltinDomainSid: int
WinBuiltinEventLogReadersGroup: int
WinBuiltinGuestsSid: int
WinBuiltinIUsersSid: int
WinBuiltinIncomingForestTrustBuildersSid: int
WinBuiltinNetworkConfigurationOperatorsSid: int
WinBuiltinPerfLoggingUsersSid: int
WinBuiltinPerfMonitoringUsersSid: int
WinBuiltinPowerUsersSid: int
WinBuiltinPreWindows2000CompatibleAccessSid: int
WinBuiltinPrintOperatorsSid: int
WinBuiltinRemoteDesktopUsersSid: int
WinBuiltinReplicatorSid: int
WinBuiltinSystemOperatorsSid: int
WinBuiltinTerminalServerLicenseServersSid: int
WinBuiltinUsersSid: int
WinCacheablePrincipalsGroupSid: int
WinCreatorGroupServerSid: int
WinCreatorGroupSid: int
WinCreatorOwnerRightsSid: int
WinCreatorOwnerServerSid: int
WinCreatorOwnerSid: int
WinDialupSid: int
WinDigestAuthenticationSid: int
WinEnterpriseControllersSid: int
WinEnterpriseReadonlyControllersSid: int
WinHighLabelSid: int
WinIUserSid: int
WinInteractiveSid: int
WinLocalServiceSid: int
WinLocalSid: int
WinLocalSystemSid: int
WinLogonIdsSid: int
WinLowLabelSid: int
WinMediumLabelSid: int
WinNTLMAuthenticationSid: int
WinNetworkServiceSid: int
WinNetworkSid: int
WinNonCacheablePrincipalsGroupSid: int
WinNtAuthoritySid: int
WinNullSid: int
WinOtherOrganizationSid: int
WinProxySid: int
WinRemoteLogonIdSid: int
WinRestrictedCodeSid: int
WinSChannelAuthenticationSid: int
WinSelfSid: int
WinServiceSid: int
WinSystemLabelSid: int
WinTerminalServerSid: int
WinThisOrganizationSid: int
WinUntrustedLabelSid: int
WinWorldSid: int
WinWriteRestrictedCodeSid: int
