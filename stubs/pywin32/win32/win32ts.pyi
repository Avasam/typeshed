from typing import Any

NOTIFY_FOR_ALL_SESSIONS: int
NOTIFY_FOR_THIS_SESSION: int
WTSActive: int
WTSApplicationName: int
WTSClientAddress: int
WTSClientBuildNumber: int
WTSClientDirectory: int
WTSClientDisplay: int
WTSClientHardwareId: int
WTSClientName: int
WTSClientProductId: int
WTSClientProtocolType: int
WTSConnectQuery: int
WTSConnectState: int
WTSConnected: int
WTSDisconnected: int
WTSDomainName: int
WTSDown: int
WTSIdle: int
WTSInit: int
WTSInitialProgram: int
WTSListen: int
WTSOEMId: int
WTSReset: int
WTSSessionId: int
WTSShadow: int
WTSUserConfigBrokenTimeoutSettings: int
WTSUserConfigInitialProgram: int
WTSUserConfigModemCallbackPhoneNumber: int
WTSUserConfigModemCallbackSettings: int
WTSUserConfigReconnectSettings: int
WTSUserConfigShadowingSettings: int
WTSUserConfigTerminalServerHomeDir: int
WTSUserConfigTerminalServerHomeDirDrive: int
WTSUserConfigTerminalServerProfilePath: int
WTSUserConfigTimeoutSettingsConnections: int
WTSUserConfigTimeoutSettingsDisconnections: int
WTSUserConfigTimeoutSettingsIdle: int
WTSUserConfigWorkingDirectory: int
WTSUserConfigfAllowLogonTerminalServer: int
WTSUserConfigfDeviceClientDefaultPrinter: int
WTSUserConfigfDeviceClientDrives: int
WTSUserConfigfDeviceClientPrinters: int
WTSUserConfigfInheritInitialProgram: int
WTSUserConfigfTerminalServerRemoteHomeDir: int
WTSUserName: int
WTSVirtualClientData: int
WTSVirtualFileHandle: int
WTSWinStationName: int
WTSWorkingDirectory: int
WTS_CURRENT_SERVER: int
WTS_CURRENT_SERVER_HANDLE: int
WTS_CURRENT_SERVER_NAME: None
WTS_CURRENT_SESSION: int
WTS_EVENT_ALL: int
WTS_EVENT_CONNECT: int
WTS_EVENT_CREATE: int
WTS_EVENT_DELETE: int
WTS_EVENT_DISCONNECT: int
WTS_EVENT_FLUSH: int
WTS_EVENT_LICENSE: int
WTS_EVENT_LOGOFF: int
WTS_EVENT_LOGON: int
WTS_EVENT_NONE: int
WTS_EVENT_RENAME: int
WTS_EVENT_STATECHANGE: int
WTS_PROTOCOL_TYPE_CONSOLE: int
WTS_PROTOCOL_TYPE_ICA: int
WTS_PROTOCOL_TYPE_RDP: int
WTS_WSD_FASTREBOOT: int
WTS_WSD_LOGOFF: int
WTS_WSD_POWEROFF: int
WTS_WSD_REBOOT: int
WTS_WSD_SHUTDOWN: int

def ProcessIdToSessionId(*args, **kwargs) -> Any: ...
def WTSCloseServer(*args, **kwargs) -> Any: ...
def WTSDisconnectSession(*args, **kwargs) -> Any: ...
def WTSEnumerateProcesses(*args, **kwargs) -> Any: ...
def WTSEnumerateServers(*args, **kwargs) -> Any: ...
def WTSEnumerateSessions(*args, **kwargs) -> Any: ...
def WTSGetActiveConsoleSessionId(*args, **kwargs) -> Any: ...
def WTSLogoffSession(*args, **kwargs) -> Any: ...
def WTSOpenServer(*args, **kwargs) -> Any: ...
def WTSQuerySessionInformation(*args, **kwargs) -> Any: ...
def WTSQueryUserConfig(*args, **kwargs) -> Any: ...
def WTSQueryUserToken(*args, **kwargs) -> Any: ...
def WTSRegisterSessionNotification(*args, **kwargs) -> Any: ...
def WTSSendMessage(*args, **kwargs) -> Any: ...
def WTSSetUserConfig(*args, **kwargs) -> Any: ...
def WTSShutdownSystem(*args, **kwargs) -> Any: ...
def WTSTerminateProcess(*args, **kwargs) -> Any: ...
def WTSUnRegisterSessionNotification(*args, **kwargs) -> Any: ...
def WTSWaitSystemEvent(*args, **kwargs) -> Any: ...
