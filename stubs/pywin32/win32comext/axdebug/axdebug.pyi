# Can't generate with stubgen because "ImportError: DLL load failed while importing axdebug: The specified module could not be found."
from _typeshed import Incomplete

# from win32.lib.pywintypes import IID  # Crashes stubtest
from typing_extensions import Literal, TypeAlias

IID: TypeAlias = Incomplete

APPBREAKFLAG_DEBUGGER_BLOCK: Literal[1]
APPBREAKFLAG_DEBUGGER_HALT: Literal[2]
APPBREAKFLAG_IN_BREAKPOINT: Literal[-2147483648]
APPBREAKFLAG_STEP: Literal[65536]
APPBREAKFLAG_STEPTYPE_BYTECODE: Literal[1048576]
APPBREAKFLAG_STEPTYPE_MACHINE: Literal[2097152]
APPBREAKFLAG_STEPTYPE_MASK: Literal[15728640]
APPBREAKFLAG_STEPTYPE_SOURCE: Literal[0]
BREAKPOINT_DELETED: Literal[0]
BREAKPOINT_DISABLED: Literal[1]
BREAKPOINT_ENABLED: Literal[2]
BREAKREASON_BREAKPOINT: Literal[1]
BREAKREASON_DEBUGGER_BLOCK: Literal[2]
BREAKREASON_DEBUGGER_HALT: Literal[5]
BREAKREASON_ERROR: Literal[6]
BREAKREASON_HOST_INITIATED: Literal[3]
BREAKREASON_LANGUAGE_INITIATED: Literal[4]
BREAKREASON_STEP: Literal[0]
BREAKRESUMEACTION_ABORT: Literal[0]
BREAKRESUMEACTION_CONTINUE: Literal[1]
BREAKRESUMEACTION_STEP_INTO: Literal[2]
BREAKRESUMEACTION_STEP_OUT: Literal[4]
BREAKRESUMEACTION_STEP_OVER: Literal[3]
CLSID_DefaultDebugSessionProvider: IID
CLSID_MachineDebugManager: IID
CLSID_ProcessDebugManager: IID
DBGPROP_ATTRIB_ACCESS_FINAL: Literal[32768]
DBGPROP_ATTRIB_ACCESS_PRIVATE: Literal[8192]
DBGPROP_ATTRIB_ACCESS_PROTECTED: Literal[16384]
DBGPROP_ATTRIB_ACCESS_PUBLIC: Literal[4096]
DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS: Literal[8388608]
DBGPROP_ATTRIB_NO_ATTRIB: Literal[0]
DBGPROP_ATTRIB_STORAGE_FIELD: Literal[262144]
DBGPROP_ATTRIB_STORAGE_GLOBAL: Literal[65536]
DBGPROP_ATTRIB_STORAGE_STATIC: Literal[131072]
DBGPROP_ATTRIB_STORAGE_VIRTUAL: Literal[524288]
DBGPROP_ATTRIB_TYPE_IS_CONSTANT: Literal[1048576]
DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED: Literal[2097152]
DBGPROP_ATTRIB_TYPE_IS_VOLATILE: Literal[4194304]
DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE: Literal[16]
DBGPROP_ATTRIB_VALUE_IS_INVALID: Literal[8]
DBGPROP_ATTRIB_VALUE_READONLY: Literal[2048]
DBGPROP_INFO_ATTRIBUTES: Literal[8]
DBGPROP_INFO_AUTOEXPAND: Literal[134217728]
DBGPROP_INFO_DEBUGPROP: Literal[16]
DBGPROP_INFO_FULLNAME: Literal[32]
DBGPROP_INFO_NAME: Literal[1]
DBGPROP_INFO_TYPE: Literal[2]
DBGPROP_INFO_VALUE: Literal[4]
DEBUG_TEXT_ALLOWBREAKPOINTS: Literal[8]
DEBUG_TEXT_ISEXPRESSION: Literal[1]
DOCUMENTNAMETYPE_APPNODE: Literal[0]
DOCUMENTNAMETYPE_FILE_TAIL: Literal[2]
DOCUMENTNAMETYPE_TITLE: Literal[1]
DOCUMENTNAMETYPE_URL: Literal[3]
ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller: Literal[1]
ERRORRESUMEACTION_ReexecuteErrorStatement: Literal[0]
ERRORRESUMEACTION_SkipErrorStatement: Literal[2]
EX_DBGPROP_INFO_DEBUGEXTPROP: Literal[4096]
EX_DBGPROP_INFO_ID: Literal[256]
EX_DBGPROP_INFO_LOCKBYTES: Literal[2048]
EX_DBGPROP_INFO_NTYPE: Literal[512]
EX_DBGPROP_INFO_NVALUE: Literal[1024]

def GetStackAddress(): ...
def GetThreadStateHandle(): ...

IID_IActiveScriptDebug: IID
IID_IActiveScriptErrorDebug: IID
IID_IActiveScriptSiteDebug: IID
IID_IApplicationDebugger: IID
IID_IDebugApplication: IID
IID_IDebugApplicationNode: IID
IID_IDebugApplicationNodeEvents: IID
IID_IDebugApplicationThread: IID
IID_IDebugCodeContext: IID
IID_IDebugDocument: IID
IID_IDebugDocumentContext: IID
IID_IDebugDocumentHelper: IID
IID_IDebugDocumentHost: IID
IID_IDebugDocumentInfo: IID
IID_IDebugDocumentProvider: IID
IID_IDebugDocumentText: IID
IID_IDebugDocumentTextAuthor: IID
IID_IDebugDocumentTextEvents: IID
IID_IDebugDocumentTextExternalAuthor: IID
IID_IDebugExpression: IID
IID_IDebugExpressionCallBack: IID
IID_IDebugExpressionContext: IID
IID_IDebugProperty: IID
IID_IDebugSessionProvider: IID
IID_IDebugStackFrame: IID
IID_IDebugStackFrameSniffer: IID
IID_IDebugStackFrameSnifferEx: IID
IID_IDebugSyncOperation: IID
IID_IEnumDebugApplicationNodes: IID
IID_IEnumDebugCodeContexts: IID
IID_IEnumDebugExpressionContexts: IID
IID_IEnumDebugPropertyInfo: IID
IID_IEnumDebugStackFrames: IID
IID_IEnumRemoteDebugApplicationThreads: IID
IID_IEnumRemoteDebugApplications: IID
IID_IMachineDebugManager: IID
IID_IMachineDebugManagerEvents: IID
IID_IProcessDebugManager: IID
IID_IProvideExpressionContexts: IID
IID_IRemoteDebugApplication: IID
IID_IRemoteDebugApplicationEvents: IID
IID_IRemoteDebugApplicationThread: IID
SOURCETEXT_ATTR_COMMENT: Literal[2]
SOURCETEXT_ATTR_FUNCTION_START: Literal[64]
SOURCETEXT_ATTR_KEYWORD: Literal[1]
SOURCETEXT_ATTR_NONSOURCE: Literal[4]
SOURCETEXT_ATTR_NUMBER: Literal[16]
SOURCETEXT_ATTR_OPERATOR: Literal[8]
SOURCETEXT_ATTR_STRING: Literal[32]

def SetThreadStateTrace(): ...

TEXT_DOC_ATTR_READONLY: Literal[1]
