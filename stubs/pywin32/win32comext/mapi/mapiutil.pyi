from _typeshed import Incomplete

from . import mapi as mapi, mapitags as mapitags

TupleType = tuple
ListType = list
IntType = int
prTable: Incomplete

def GetPropTagName(pt): ...

mapiErrorTable: Incomplete

def GetScodeString(hr): ...

ptTable: Incomplete

def GetMapiTypeName(propType, rawType: bool = ...): ...
def GetProperties(obj, propList): ...
def GetAllProperties(obj, make_tag_names: bool = ...): ...
def SetPropertyValue(obj, prop, val) -> None: ...
def SetProperties(msg, propDict) -> None: ...
