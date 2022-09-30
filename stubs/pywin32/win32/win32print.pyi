from typing import Any

DEF_PRIORITY: int
DI_APPBANDING: int
DI_ROPS_READ_DESTINATION: int
DPD_DELETE_ALL_FILES: int
DPD_DELETE_SPECIFIC_VERSION: int
DPD_DELETE_UNUSED_FILES: int
DSPRINT_PENDING: int
DSPRINT_PUBLISH: int
DSPRINT_REPUBLISH: int
DSPRINT_UNPUBLISH: int
DSPRINT_UPDATE: int
FORM_BUILTIN: int
FORM_PRINTER: int
FORM_USER: int
JOB_ACCESS_ADMINISTER: int
JOB_ACCESS_READ: int
JOB_ALL_ACCESS: int
JOB_CONTROL_CANCEL: int
JOB_CONTROL_DELETE: int
JOB_CONTROL_LAST_PAGE_EJECTED: int
JOB_CONTROL_PAUSE: int
JOB_CONTROL_RESTART: int
JOB_CONTROL_RESUME: int
JOB_CONTROL_SENT_TO_PRINTER: int
JOB_EXECUTE: int
JOB_INFO_1: int
JOB_POSITION_UNSPECIFIED: int
JOB_READ: int
JOB_STATUS_BLOCKED_DEVQ: int
JOB_STATUS_COMPLETE: int
JOB_STATUS_DELETED: int
JOB_STATUS_DELETING: int
JOB_STATUS_ERROR: int
JOB_STATUS_OFFLINE: int
JOB_STATUS_PAPEROUT: int
JOB_STATUS_PAUSED: int
JOB_STATUS_PRINTED: int
JOB_STATUS_PRINTING: int
JOB_STATUS_RESTART: int
JOB_STATUS_SPOOLING: int
JOB_STATUS_USER_INTERVENTION: int
JOB_WRITE: int
MAX_PRIORITY: int
MIN_PRIORITY: int
PORT_STATUS_DOOR_OPEN: int
PORT_STATUS_NO_TONER: int
PORT_STATUS_OFFLINE: int
PORT_STATUS_OUTPUT_BIN_FULL: int
PORT_STATUS_OUT_OF_MEMORY: int
PORT_STATUS_PAPER_JAM: int
PORT_STATUS_PAPER_OUT: int
PORT_STATUS_PAPER_PROBLEM: int
PORT_STATUS_POWER_SAVE: int
PORT_STATUS_TONER_LOW: int
PORT_STATUS_TYPE_ERROR: int
PORT_STATUS_TYPE_INFO: int
PORT_STATUS_TYPE_WARNING: int
PORT_STATUS_USER_INTERVENTION: int
PORT_STATUS_WARMING_UP: int
PORT_TYPE_NET_ATTACHED: int
PORT_TYPE_READ: int
PORT_TYPE_REDIRECTED: int
PORT_TYPE_WRITE: int
PRINTER_ACCESS_ADMINISTER: int
PRINTER_ACCESS_USE: int
PRINTER_ALL_ACCESS: int
PRINTER_ATTRIBUTE_DEFAULT: int
PRINTER_ATTRIBUTE_DIRECT: int
PRINTER_ATTRIBUTE_DO_COMPLETE_FIRST: int
PRINTER_ATTRIBUTE_ENABLE_BIDI: int
PRINTER_ATTRIBUTE_ENABLE_DEVQ: int
PRINTER_ATTRIBUTE_FAX: int
PRINTER_ATTRIBUTE_HIDDEN: int
PRINTER_ATTRIBUTE_KEEPPRINTEDJOBS: int
PRINTER_ATTRIBUTE_LOCAL: int
PRINTER_ATTRIBUTE_NETWORK: int
PRINTER_ATTRIBUTE_PUBLISHED: int
PRINTER_ATTRIBUTE_QUEUED: int
PRINTER_ATTRIBUTE_RAW_ONLY: int
PRINTER_ATTRIBUTE_SHARED: int
PRINTER_ATTRIBUTE_TS: int
PRINTER_ATTRIBUTE_WORK_OFFLINE: int
PRINTER_CONTROL_PAUSE: int
PRINTER_CONTROL_PURGE: int
PRINTER_CONTROL_RESUME: int
PRINTER_CONTROL_SET_STATUS: int
PRINTER_ENUM_CONNECTIONS: int
PRINTER_ENUM_CONTAINER: int
PRINTER_ENUM_DEFAULT: int
PRINTER_ENUM_EXPAND: int
PRINTER_ENUM_ICON1: int
PRINTER_ENUM_ICON2: int
PRINTER_ENUM_ICON3: int
PRINTER_ENUM_ICON4: int
PRINTER_ENUM_ICON5: int
PRINTER_ENUM_ICON6: int
PRINTER_ENUM_ICON7: int
PRINTER_ENUM_ICON8: int
PRINTER_ENUM_LOCAL: int
PRINTER_ENUM_NAME: int
PRINTER_ENUM_NETWORK: int
PRINTER_ENUM_REMOTE: int
PRINTER_ENUM_SHARED: int
PRINTER_EXECUTE: int
PRINTER_INFO_1: int
PRINTER_READ: int
PRINTER_STATUS_BUSY: int
PRINTER_STATUS_DOOR_OPEN: int
PRINTER_STATUS_ERROR: int
PRINTER_STATUS_INITIALIZING: int
PRINTER_STATUS_IO_ACTIVE: int
PRINTER_STATUS_MANUAL_FEED: int
PRINTER_STATUS_NOT_AVAILABLE: int
PRINTER_STATUS_NO_TONER: int
PRINTER_STATUS_OFFLINE: int
PRINTER_STATUS_OUTPUT_BIN_FULL: int
PRINTER_STATUS_OUT_OF_MEMORY: int
PRINTER_STATUS_PAGE_PUNT: int
PRINTER_STATUS_PAPER_JAM: int
PRINTER_STATUS_PAPER_OUT: int
PRINTER_STATUS_PAPER_PROBLEM: int
PRINTER_STATUS_PAUSED: int
PRINTER_STATUS_PENDING_DELETION: int
PRINTER_STATUS_POWER_SAVE: int
PRINTER_STATUS_PRINTING: int
PRINTER_STATUS_PROCESSING: int
PRINTER_STATUS_SERVER_UNKNOWN: int
PRINTER_STATUS_TONER_LOW: int
PRINTER_STATUS_USER_INTERVENTION: int
PRINTER_STATUS_WAITING: int
PRINTER_STATUS_WARMING_UP: int
PRINTER_WRITE: int
SERVER_ACCESS_ADMINISTER: int
SERVER_ACCESS_ENUMERATE: int
SERVER_ALL_ACCESS: int
SERVER_EXECUTE: int
SERVER_READ: int
SERVER_WRITE: int

def AbortDoc(*args, **kwargs) -> Any: ...
def AbortPrinter(*args, **kwargs) -> Any: ...
def AddForm(*args, **kwargs) -> Any: ...
def AddJob(*args, **kwargs) -> Any: ...
def AddPrinter(*args, **kwargs) -> Any: ...
def AddPrinterConnection(*args, **kwargs) -> Any: ...
def ClosePrinter(*args, **kwargs) -> Any: ...
def DeleteForm(*args, **kwargs) -> Any: ...
def DeletePrinter(*args, **kwargs) -> Any: ...
def DeletePrinterConnection(*args, **kwargs) -> Any: ...
def DeletePrinterDriver(*args, **kwargs) -> Any: ...
def DeletePrinterDriverEx(*args, **kwargs) -> Any: ...
def DeviceCapabilities(*args, **kwargs) -> Any: ...
def DocumentProperties(*args, **kwargs) -> Any: ...
def EndDoc(*args, **kwargs) -> Any: ...
def EndDocPrinter(*args, **kwargs) -> Any: ...
def EndPage(*args, **kwargs) -> Any: ...
def EndPagePrinter(*args, **kwargs) -> Any: ...
def EnumForms(*args, **kwargs) -> Any: ...
def EnumJobs(*args, **kwargs) -> Any: ...
def EnumMonitors(*args, **kwargs) -> Any: ...
def EnumPorts(*args, **kwargs) -> Any: ...
def EnumPrintProcessorDatatypes(*args, **kwargs) -> Any: ...
def EnumPrintProcessors(*args, **kwargs) -> Any: ...
def EnumPrinterDrivers(*args, **kwargs) -> Any: ...
def EnumPrinters(*args, **kwargs) -> Any: ...
def FlushPrinter(*args, **kwargs) -> Any: ...
def GetDefaultPrinter(*args, **kwargs) -> Any: ...
def GetDefaultPrinterW(*args, **kwargs) -> Any: ...
def GetDeviceCaps(*args, **kwargs) -> Any: ...
def GetForm(*args, **kwargs) -> Any: ...
def GetJob(*args, **kwargs) -> Any: ...
def GetPrintProcessorDirectory(*args, **kwargs) -> Any: ...
def GetPrinter(*args, **kwargs) -> Any: ...
def GetPrinterDriverDirectory(*args, **kwargs) -> Any: ...
def OpenPrinter(*args, **kwargs) -> Any: ...
def ScheduleJob(*args, **kwargs) -> Any: ...
def SetDefaultPrinter(*args, **kwargs) -> Any: ...
def SetDefaultPrinterW(*args, **kwargs) -> Any: ...
def SetForm(*args, **kwargs) -> Any: ...
def SetJob(*args, **kwargs) -> Any: ...
def SetPrinter(*args, **kwargs) -> Any: ...
def StartDoc(*args, **kwargs) -> Any: ...
def StartDocPrinter(*args, **kwargs) -> Any: ...
def StartPage(*args, **kwargs) -> Any: ...
def StartPagePrinter(*args, **kwargs) -> Any: ...
def WritePrinter(*args, **kwargs) -> Any: ...
