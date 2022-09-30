from typing import Any

RASCS_AllDevicesConnected: int
RASCS_AuthAck: int
RASCS_AuthCallback: int
RASCS_AuthChangePassword: int
RASCS_AuthLinkSpeed: int
RASCS_AuthNotify: int
RASCS_AuthProject: int
RASCS_AuthRetry: int
RASCS_Authenticate: int
RASCS_Authenticated: int
RASCS_CallbackComplete: int
RASCS_CallbackSetByCaller: int
RASCS_ConnectDevice: int
RASCS_Connected: int
RASCS_DeviceConnected: int
RASCS_Disconnected: int
RASCS_Interactive: int
RASCS_LogonNetwork: int
RASCS_OpenPort: int
RASCS_PasswordExpired: int
RASCS_PortOpened: int
RASCS_PrepareForCallback: int
RASCS_Projected: int
RASCS_ReAuthenticate: int
RASCS_RetryAuthentication: int
RASCS_StartAuthentication: int
RASCS_WaitForCallback: int
RASCS_WaitForModemReset: int
RASEAPF_Logon: int
RASEAPF_NonInteractive: int
RASEAPF_Preview: int

class error(Exception): ...

def CreatePhonebookEntry(*args, **kwargs) -> Any: ...
def Dial(*args, **kwargs) -> Any: ...
def EditPhonebookEntry(*args, **kwargs) -> Any: ...
def EnumConnections(*args, **kwargs) -> Any: ...
def EnumEntries(*args, **kwargs) -> Any: ...
def GetConnectStatus(*args, **kwargs) -> Any: ...
def GetEapUserIdentity(*args, **kwargs) -> Any: ...
def GetEntryDialParams(*args, **kwargs) -> Any: ...
def GetErrorString(*args, **kwargs) -> Any: ...
def HangUp(*args, **kwargs) -> Any: ...
def IsHandleValid(*args, **kwargs) -> Any: ...
def RASDIALEXTENSIONS(*args, **kwargs) -> Any: ...
def SetEntryDialParams(*args, **kwargs) -> Any: ...
