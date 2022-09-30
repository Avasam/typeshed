from typing import Any

ETDT_DISABLE: int
ETDT_ENABLE: int
ETDT_ENABLETAB: int
ETDT_USETABTEXTURE: int
UNICODE: int

class error(Exception): ...

def CloseThemeData(*args, **kwargs) -> Any: ...
def DrawThemeBackground(*args, **kwargs) -> Any: ...
def DrawThemeText(*args, **kwargs) -> Any: ...
def EnableThemeDialogTexture(*args, **kwargs) -> Any: ...
def EnableTheming(*args, **kwargs) -> Any: ...
def GetCurrentThemeName(*args, **kwargs) -> Any: ...
def GetThemeAppProperties(*args, **kwargs) -> Any: ...
def GetThemeBackgroundContentRect(*args, **kwargs) -> Any: ...
def GetThemeBackgroundExtent(*args, **kwargs) -> Any: ...
def GetWindowTheme(*args, **kwargs) -> Any: ...
def IsAppThemed(*args, **kwargs) -> Any: ...
def IsThemeActive(*args, **kwargs) -> Any: ...
def IsThemeDialogTextureEnabled(*args, **kwargs) -> Any: ...
def OpenThemeData(*args, **kwargs) -> Any: ...
def SetWindowTheme(*args, **kwargs) -> Any: ...
