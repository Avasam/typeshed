from typing import Any

SERVICE_SERVER: str
SERVICE_WORKSTATION: str
USE_FORCE: int
USE_LOTS_OF_FORCE: int
USE_NOFORCE: int

class error(Exception): ...

def NetFileClose(*args, **kwargs) -> Any: ...
def NetFileEnum(*args, **kwargs) -> Any: ...
def NetFileGetInfo(*args, **kwargs) -> Any: ...
def NetGetAnyDCName(*args, **kwargs) -> Any: ...
def NetGetDCName(*args, **kwargs) -> Any: ...
def NetGetJoinInformation(*args, **kwargs) -> Any: ...
def NetGroupAdd(*args, **kwargs) -> Any: ...
def NetGroupAddUser(*args, **kwargs) -> Any: ...
def NetGroupDel(*args, **kwargs) -> Any: ...
def NetGroupDelUser(*args, **kwargs) -> Any: ...
def NetGroupEnum(*args, **kwargs) -> Any: ...
def NetGroupGetInfo(*args, **kwargs) -> Any: ...
def NetGroupGetUsers(*args, **kwargs) -> Any: ...
def NetGroupSetInfo(*args, **kwargs) -> Any: ...
def NetGroupSetUsers(*args, **kwargs) -> Any: ...
def NetLocalGroupAdd(*args, **kwargs) -> Any: ...
def NetLocalGroupAddMembers(*args, **kwargs) -> Any: ...
def NetLocalGroupDel(*args, **kwargs) -> Any: ...
def NetLocalGroupDelMembers(*args, **kwargs) -> Any: ...
def NetLocalGroupEnum(*args, **kwargs) -> Any: ...
def NetLocalGroupGetInfo(*args, **kwargs) -> Any: ...
def NetLocalGroupGetMembers(*args, **kwargs) -> Any: ...
def NetLocalGroupSetInfo(*args, **kwargs) -> Any: ...
def NetLocalGroupSetMembers(*args, **kwargs) -> Any: ...
def NetMessageBufferSend(*args, **kwargs) -> Any: ...
def NetMessageNameAdd(*args, **kwargs) -> Any: ...
def NetMessageNameDel(*args, **kwargs) -> Any: ...
def NetMessageNameEnum(*args, **kwargs) -> Any: ...
def NetServerComputerNameAdd(*args, **kwargs) -> Any: ...
def NetServerComputerNameDel(*args, **kwargs) -> Any: ...
def NetServerDiskEnum(*args, **kwargs) -> Any: ...
def NetServerEnum(*args, **kwargs) -> Any: ...
def NetServerGetInfo(*args, **kwargs) -> Any: ...
def NetServerSetInfo(*args, **kwargs) -> Any: ...
def NetSessionDel(*args, **kwargs) -> Any: ...
def NetSessionEnum(*args, **kwargs) -> Any: ...
def NetSessionGetInfo(*args, **kwargs) -> Any: ...
def NetShareAdd(*args, **kwargs) -> Any: ...
def NetShareCheck(*args, **kwargs) -> Any: ...
def NetShareDel(*args, **kwargs) -> Any: ...
def NetShareEnum(*args, **kwargs) -> Any: ...
def NetShareGetInfo(*args, **kwargs) -> Any: ...
def NetShareSetInfo(*args, **kwargs) -> Any: ...
def NetStatisticsGet(*args, **kwargs) -> Any: ...
def NetUseAdd(*args, **kwargs) -> Any: ...
def NetUseDel(*args, **kwargs) -> Any: ...
def NetUseEnum(*args, **kwargs) -> Any: ...
def NetUseGetInfo(*args, **kwargs) -> Any: ...
def NetUserAdd(*args, **kwargs) -> Any: ...
def NetUserChangePassword(*args, **kwargs) -> Any: ...
def NetUserDel(*args, **kwargs) -> Any: ...
def NetUserEnum(*args, **kwargs) -> Any: ...
def NetUserGetGroups(*args, **kwargs) -> Any: ...
def NetUserGetInfo(*args, **kwargs) -> Any: ...
def NetUserGetLocalGroups(*args, **kwargs) -> Any: ...
def NetUserModalsGet(*args, **kwargs) -> Any: ...
def NetUserModalsSet(*args, **kwargs) -> Any: ...
def NetUserSetInfo(*args, **kwargs) -> Any: ...
def NetValidateName(*args, **kwargs) -> Any: ...
def NetValidatePasswordPolicy(*args, **kwargs) -> Any: ...
def NetWkstaGetInfo(*args, **kwargs) -> Any: ...
def NetWkstaSetInfo(*args, **kwargs) -> Any: ...
def NetWkstaTransportAdd(*args, **kwargs) -> Any: ...
def NetWkstaTransportDel(*args, **kwargs) -> Any: ...
def NetWkstaTransportEnum(*args, **kwargs) -> Any: ...
def NetWkstaUserEnum(*args, **kwargs) -> Any: ...
