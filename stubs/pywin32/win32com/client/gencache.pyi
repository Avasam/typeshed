from _typeshed import Incomplete

from . import CLSIDToClass as CLSIDToClass

bForDemandDefault: int
clsidToTypelib: Incomplete
versionRedirectMap: Incomplete
is_readonly: Incomplete
is_zip: Incomplete
demandGeneratedTypeLibraries: Incomplete

def __init__() -> None: ...

pickleVersion: int

def GetGeneratedFileName(clsid, lcid, major, minor): ...
def SplitGeneratedFileName(fname): ...
def GetGeneratePath(): ...
def GetClassForProgID(progid): ...
def GetClassForCLSID(clsid): ...
def GetModuleForProgID(progid): ...
def GetModuleForCLSID(clsid): ...
def GetModuleForTypelib(typelibCLSID, lcid, major, minor): ...
def MakeModuleForTypelib(
    typelibCLSID, lcid, major, minor, progressInstance: Incomplete | None = ..., bForDemand=..., bBuildHidden: int = ...
): ...
def MakeModuleForTypelibInterface(
    typelib_ob, progressInstance: Incomplete | None = ..., bForDemand=..., bBuildHidden: int = ...
): ...
def EnsureModuleForTypelibInterface(
    typelib_ob, progressInstance: Incomplete | None = ..., bForDemand=..., bBuildHidden: int = ...
): ...
def ForgetAboutTypelibInterface(typelib_ob) -> None: ...
def EnsureModule(
    typelibCLSID,
    lcid,
    major,
    minor,
    progressInstance: Incomplete | None = ...,
    bValidateFile=...,
    bForDemand=...,
    bBuildHidden: int = ...,
): ...
def EnsureDispatch(prog_id, bForDemand: int = ...): ...
def AddModuleToCache(typelibclsid, lcid, major, minor, verbose: int = ..., bFlushNow=...) -> None: ...
def GetGeneratedInfos(): ...
def Rebuild(verbose: int = ...) -> None: ...
def usage() -> None: ...
