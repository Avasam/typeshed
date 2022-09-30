from typing import Any
from typing_extensions import final

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
DS_SPN_DNS_HOST: int
DS_SPN_DN_HOST: int
DS_SPN_DOMAIN: int
DS_SPN_NB_DOMAIN: int
DS_SPN_NB_HOST: int
DS_SPN_REPLACE_SPN_OP: int
DS_SPN_SERVICE: int
FAILED_ACCESS_ACE_FLAG: int
GRANT_ACCESS: int
GROUP_SECURITY_INFORMATION: int
INHERITED_ACE: int
INHERIT_ONLY_ACE: int
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
MICROSOFT_KERBEROS_NAME_A: bytes
MSV1_0_PACKAGE_NAME: bytes
NOT_USED_ACCESS: int
NO_INHERITANCE: int
NO_PROPAGATE_INHERIT_ACE: int
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
PROTECTED_DACL_SECURITY_INFORMATION: int
PROTECTED_SACL_SECURITY_INFORMATION: int
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
REVOKE_ACCESS: int
SACL_SECURITY_INFORMATION: int
SANDBOX_INERT: int
SDDL_REVISION_1: int
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
SET_ACCESS: int
SET_AUDIT_FAILURE: int
SET_AUDIT_SUCCESS: int
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
SE_DACL_AUTO_INHERITED: int
SE_DACL_DEFAULTED: int
SE_DACL_PRESENT: int
SE_DACL_PROTECTED: int
SE_DEBUG_NAME: str
SE_DENY_BATCH_LOGON_NAME: str
SE_DENY_INTERACTIVE_LOGON_NAME: str
SE_DENY_NETWORK_LOGON_NAME: str
SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_DENY_SERVICE_LOGON_NAME: str
SE_DS_OBJECT: int
SE_DS_OBJECT_ALL: int
SE_ENABLE_DELEGATION_NAME: str
SE_FILE_OBJECT: int
SE_GROUP_DEFAULTED: int
SE_GROUP_ENABLED: int
SE_GROUP_ENABLED_BY_DEFAULT: int
SE_GROUP_INTEGRITY: int
SE_GROUP_INTEGRITY_ENABLED: int
SE_GROUP_LOGON_ID: int
SE_GROUP_MANDATORY: int
SE_GROUP_OWNER: int
SE_GROUP_RESOURCE: int
SE_GROUP_USE_FOR_DENY_ONLY: int
SE_IMPERSONATE_NAME: str
SE_INCREASE_QUOTA_NAME: str
SE_INC_BASE_PRIORITY_NAME: str
SE_INC_WORKING_SET_NAME: str
SE_INTERACTIVE_LOGON_NAME: str
SE_KERNEL_OBJECT: int
SE_LMSHARE: int
SE_LOAD_DRIVER_NAME: str
SE_LOCK_MEMORY_NAME: str
SE_MACHINE_ACCOUNT_NAME: str
SE_MANAGE_VOLUME_NAME: str
SE_NETWORK_LOGON_NAME: str
SE_OWNER_DEFAULTED: int
SE_PRINTER: int
SE_PRIVILEGE_ENABLED: int
SE_PRIVILEGE_ENABLED_BY_DEFAULT: int
SE_PRIVILEGE_REMOVED: int
SE_PRIVILEGE_USED_FOR_ACCESS: int
SE_PROF_SINGLE_PROCESS_NAME: str
SE_PROVIDER_DEFINED_OBJECT: int
SE_REGISTRY_KEY: int
SE_REGISTRY_WOW64_32KEY: int
SE_RELABEL_NAME: str
SE_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_REMOTE_SHUTDOWN_NAME: str
SE_RESTORE_NAME: str
SE_SACL_AUTO_INHERITED: int
SE_SACL_DEFAULTED: int
SE_SACL_PRESENT: int
SE_SACL_PROTECTED: int
SE_SECURITY_NAME: str
SE_SELF_RELATIVE: int
SE_SERVICE: int
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
SE_UNKNOWN_OBJECT_TYPE: int
SE_UNSOLICITED_INPUT_NAME: str
SE_WINDOW_OBJECT: int
SE_WMIGUID_OBJECT: int
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
SYSTEM_MANDATORY_LABEL_NO_EXECUTE_UP: int
SYSTEM_MANDATORY_LABEL_NO_READ_UP: int
SYSTEM_MANDATORY_LABEL_NO_WRITE_UP: int
SYSTEM_MANDATORY_LABEL_VALID_MASK: int
SecurityAnonymous: int
SecurityDelegation: int
SecurityIdentification: int
SecurityImpersonation: int
SidTypeAlias: int
SidTypeComputer: int
SidTypeDeletedAccount: int
SidTypeDomain: int
SidTypeGroup: int
SidTypeInvalid: int
SidTypeUnknown: int
SidTypeUser: int
SidTypeWellKnownGroup: int
TOKEN_ADJUST_DEFAULT: int
TOKEN_ADJUST_GROUPS: int
TOKEN_ADJUST_PRIVILEGES: int
TOKEN_ALL_ACCESS: int
TOKEN_ASSIGN_PRIMARY: int
TOKEN_DUPLICATE: int
TOKEN_EXECUTE: int
TOKEN_IMPERSONATE: int
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN: int
TOKEN_MANDATORY_POLICY_NO_WRITE_UP: int
TOKEN_MANDATORY_POLICY_OFF: int
TOKEN_MANDATORY_POLICY_VALID_MASK: int
TOKEN_QUERY: int
TOKEN_QUERY_SOURCE: int
TOKEN_READ: int
TOKEN_WRITE: int
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
TokenImpersonation: int
TokenImpersonationLevel: int
TokenIntegrityLevel: int
TokenLinkedToken: int
TokenLogonSid: int
TokenMandatoryPolicy: int
TokenOrigin: int
TokenOwner: int
TokenPrimary: int
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
UNICODE: int
UNPROTECTED_DACL_SECURITY_INFORMATION: int
UNPROTECTED_SACL_SECURITY_INFORMATION: int
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

@final
class CredHandleType:
    def __init__(self, *args, **kwargs) -> None: ...
    def Detach(self, *args, **kwargs) -> Any: ...
    def FreeCredentialsHandle(self, *args, **kwargs) -> Any: ...
    def QueryCredentialsAttributes(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class CtxtHandleType:
    def __init__(self, *args, **kwargs) -> None: ...
    def CompleteAuthToken(self, *args, **kwargs) -> Any: ...
    def DecryptMessage(self, *args, **kwargs) -> Any: ...
    def DeleteSecurityContext(self, *args, **kwargs) -> Any: ...
    def Detach(self, *args, **kwargs) -> Any: ...
    def EncryptMessage(self, *args, **kwargs) -> Any: ...
    def ImpersonateSecurityContext(self, *args, **kwargs) -> Any: ...
    def MakeSignature(self, *args, **kwargs) -> Any: ...
    def QueryContextAttributes(self, *args, **kwargs) -> Any: ...
    def QuerySecurityContextToken(self, *args, **kwargs) -> Any: ...
    def RevertSecurityContext(self, *args, **kwargs) -> Any: ...
    def VerifySignature(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class PyCredHandleType:
    def __init__(self, *args, **kwargs) -> None: ...
    def Detach(self, *args, **kwargs) -> Any: ...
    def FreeCredentialsHandle(self, *args, **kwargs) -> Any: ...
    def QueryCredentialsAttributes(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class PyCtxtHandleType:
    def __init__(self, *args, **kwargs) -> None: ...
    def CompleteAuthToken(self, *args, **kwargs) -> Any: ...
    def DecryptMessage(self, *args, **kwargs) -> Any: ...
    def DeleteSecurityContext(self, *args, **kwargs) -> Any: ...
    def Detach(self, *args, **kwargs) -> Any: ...
    def EncryptMessage(self, *args, **kwargs) -> Any: ...
    def ImpersonateSecurityContext(self, *args, **kwargs) -> Any: ...
    def MakeSignature(self, *args, **kwargs) -> Any: ...
    def QueryContextAttributes(self, *args, **kwargs) -> Any: ...
    def QuerySecurityContextToken(self, *args, **kwargs) -> Any: ...
    def RevertSecurityContext(self, *args, **kwargs) -> Any: ...
    def VerifySignature(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class PySecBufferDescType:
    Version: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...

@final
class PySecBufferType:
    Buffer: Any
    BufferSize: Any
    BufferType: Any
    MaxBufferSize: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def Clear(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

@final
class SecBufferDescType:
    Version: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...

@final
class SecBufferType:
    Buffer: Any
    BufferSize: Any
    BufferType: Any
    MaxBufferSize: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def Clear(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class error(Exception): ...

def ACL(*args, **kwargs) -> Any: ...
def AcceptSecurityContext(*args, **kwargs) -> Any: ...
def AcquireCredentialsHandle(*args, **kwargs) -> Any: ...
def AdjustTokenGroups(*args, **kwargs) -> Any: ...
def AdjustTokenPrivileges(*args, **kwargs) -> Any: ...
def AllocateLocallyUniqueId(*args, **kwargs) -> Any: ...
def CheckTokenMembership(*args, **kwargs) -> Any: ...
def ConvertSecurityDescriptorToStringSecurityDescriptor(*args, **kwargs) -> Any: ...
def ConvertSidToStringSid(*args, **kwargs) -> Any: ...
def ConvertStringSecurityDescriptorToSecurityDescriptor(*args, **kwargs) -> Any: ...
def ConvertStringSidToSid(*args, **kwargs) -> Any: ...
def CreateRestrictedToken(*args, **kwargs) -> Any: ...
def CreateWellKnownSid(*args, **kwargs) -> Any: ...
def CryptEnumProviders(*args, **kwargs) -> Any: ...
def DsBind(*args, **kwargs) -> Any: ...
def DsCrackNames(*args, **kwargs) -> Any: ...
def DsGetDcName(*args, **kwargs) -> Any: ...
def DsGetSpn(*args, **kwargs) -> Any: ...
def DsListDomainsInSite(*args, **kwargs) -> Any: ...
def DsListInfoForServer(*args, **kwargs) -> Any: ...
def DsListRoles(*args, **kwargs) -> Any: ...
def DsListServersForDomainInSite(*args, **kwargs) -> Any: ...
def DsListServersInSite(*args, **kwargs) -> Any: ...
def DsListSites(*args, **kwargs) -> Any: ...
def DsUnBind(*args, **kwargs) -> Any: ...
def DsWriteAccountSpn(*args, **kwargs) -> Any: ...
def DuplicateToken(*args, **kwargs) -> Any: ...
def DuplicateTokenEx(*args, **kwargs) -> Any: ...
def EnumerateSecurityPackages(*args, **kwargs) -> Any: ...
def GetBinarySid(*args, **kwargs) -> Any: ...
def GetFileSecurity(*args, **kwargs) -> Any: ...
def GetKernelObjectSecurity(*args, **kwargs) -> Any: ...
def GetNamedSecurityInfo(*args, **kwargs) -> Any: ...
def GetPolicyHandle(*args, **kwargs) -> Any: ...
def GetSecurityInfo(*args, **kwargs) -> Any: ...
def GetTokenInformation(*args, **kwargs) -> Any: ...
def GetUserObjectSecurity(*args, **kwargs) -> Any: ...
def ImpersonateAnonymousToken(*args, **kwargs) -> Any: ...
def ImpersonateLoggedOnUser(*args, **kwargs) -> Any: ...
def ImpersonateNamedPipeClient(*args, **kwargs) -> Any: ...
def ImpersonateSelf(*args, **kwargs) -> Any: ...
def InitializeSecurityContext(*args, **kwargs) -> Any: ...
def IsTokenRestricted(*args, **kwargs) -> Any: ...
def LogonUser(*args, **kwargs) -> Any: ...
def LogonUserEx(*args, **kwargs) -> Any: ...
def LookupAccountName(*args, **kwargs) -> Any: ...
def LookupAccountSid(*args, **kwargs) -> Any: ...
def LookupPrivilegeDisplayName(*args, **kwargs) -> Any: ...
def LookupPrivilegeName(*args, **kwargs) -> Any: ...
def LookupPrivilegeValue(*args, **kwargs) -> Any: ...
def LsaAddAccountRights(*args, **kwargs) -> Any: ...
def LsaCallAuthenticationPackage(*args, **kwargs) -> Any: ...
def LsaClose(*args, **kwargs) -> Any: ...
def LsaConnectUntrusted(*args, **kwargs) -> Any: ...
def LsaDeregisterLogonProcess(*args, **kwargs) -> Any: ...
def LsaEnumerateAccountRights(*args, **kwargs) -> Any: ...
def LsaEnumerateAccountsWithUserRight(*args, **kwargs) -> Any: ...
def LsaEnumerateLogonSessions(*args, **kwargs) -> Any: ...
def LsaGetLogonSessionData(*args, **kwargs) -> Any: ...
def LsaLookupAuthenticationPackage(*args, **kwargs) -> Any: ...
def LsaOpenPolicy(*args, **kwargs) -> Any: ...
def LsaQueryInformationPolicy(*args, **kwargs) -> Any: ...
def LsaRegisterLogonProcess(*args, **kwargs) -> Any: ...
def LsaRegisterPolicyChangeNotification(*args, **kwargs) -> Any: ...
def LsaRemoveAccountRights(*args, **kwargs) -> Any: ...
def LsaRetrievePrivateData(*args, **kwargs) -> Any: ...
def LsaSetInformationPolicy(*args, **kwargs) -> Any: ...
def LsaStorePrivateData(*args, **kwargs) -> Any: ...
def LsaUnregisterPolicyChangeNotification(*args, **kwargs) -> Any: ...
def MapGenericMask(*args, **kwargs) -> Any: ...
def OpenProcessToken(*args, **kwargs) -> Any: ...
def OpenThreadToken(*args, **kwargs) -> Any: ...
def QuerySecurityPackageInfo(*args, **kwargs) -> Any: ...
def RevertToSelf(*args, **kwargs) -> Any: ...
def SECURITY_ATTRIBUTES(*args, **kwargs) -> Any: ...
def SECURITY_DESCRIPTOR(*args, **kwargs) -> Any: ...
def SID(*args, **kwargs) -> Any: ...
def SetFileSecurity(*args, **kwargs) -> Any: ...
def SetKernelObjectSecurity(*args, **kwargs) -> Any: ...
def SetNamedSecurityInfo(*args, **kwargs) -> Any: ...
def SetSecurityInfo(*args, **kwargs) -> Any: ...
def SetThreadToken(*args, **kwargs) -> Any: ...
def SetTokenInformation(*args, **kwargs) -> Any: ...
def SetUserObjectSecurity(*args, **kwargs) -> Any: ...
def TranslateName(*args, **kwargs) -> Any: ...
