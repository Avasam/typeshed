# Can't generate with stubgen because "ImportError: This must be an MFC application - try 'import win32ui' first"
from typing_extensions import Literal

APPCLASS_MONITOR: Literal[1]
APPCLASS_STANDARD: Literal[0]
APPCMD_CLIENTONLY: Literal[16]
APPCMD_FILTERINITS: Literal[32]
CBF_FAIL_ADVISES: Literal[16384]
CBF_FAIL_ALLSVRXACTIONS: Literal[258048]
CBF_FAIL_CONNECTIONS: Literal[8192]
CBF_FAIL_EXECUTES: Literal[32768]
CBF_FAIL_POKES: Literal[65536]
CBF_FAIL_REQUESTS: Literal[131072]
CBF_FAIL_SELFCONNECTIONS: Literal[4096]
CBF_SKIP_ALLNOTIFICATIONS: Literal[3932160]
CBF_SKIP_CONNECT_CONFIRMS: Literal[262144]
CBF_SKIP_DISCONNECTS: Literal[2097152]
CBF_SKIP_REGISTRATIONS: Literal[524288]

def CreateConversation(): ...
def CreateServer(): ...
def CreateServerSystemTopic(): ...
def CreateStringItem(): ...
def CreateTopic(): ...

MF_CALLBACKS: Literal[134217728]
MF_CONV: Literal[1073741824]
MF_ERRORS: Literal[268435456]
MF_HSZ_INFO: Literal[16777216]
MF_LINKS: Literal[536870912]
MF_POSTMSGS: Literal[67108864]
MF_SENDMSGS: Literal[33554432]
