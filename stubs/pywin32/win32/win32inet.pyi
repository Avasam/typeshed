from typing import Any

UNICODE: int

class error(Exception): ...

def CommitUrlCacheEntry(*args, **kwargs) -> Any: ...
def CreateUrlCacheEntry(*args, **kwargs) -> Any: ...
def CreateUrlCacheGroup(*args, **kwargs) -> Any: ...
def DeleteUrlCacheEntry(*args, **kwargs) -> Any: ...
def DeleteUrlCacheGroup(*args, **kwargs) -> Any: ...
def FindCloseUrlCache(*args, **kwargs) -> Any: ...
def FindFirstUrlCacheEntry(*args, **kwargs) -> Any: ...
def FindFirstUrlCacheEntryEx(*args, **kwargs) -> Any: ...
def FindFirstUrlCacheGroup(*args, **kwargs) -> Any: ...
def FindNextUrlCacheEntry(*args, **kwargs) -> Any: ...
def FindNextUrlCacheEntryEx(*args, **kwargs) -> Any: ...
def FindNextUrlCacheGroup(*args, **kwargs) -> Any: ...
def FtpCommand(*args, **kwargs) -> Any: ...
def FtpOpenFile(*args, **kwargs) -> Any: ...
def GetUrlCacheEntryInfo(*args, **kwargs) -> Any: ...
def GetUrlCacheGroupAttribute(*args, **kwargs) -> Any: ...
def InternetAttemptConnect(*args, **kwargs) -> Any: ...
def InternetCanonicalizeUrl(*args, **kwargs) -> Any: ...
def InternetCheckConnection(*args, **kwargs) -> Any: ...
def InternetCloseHandle(*args, **kwargs) -> Any: ...
def InternetConnect(*args, **kwargs) -> Any: ...
def InternetGetCookie(*args, **kwargs) -> Any: ...
def InternetGetLastResponseInfo(*args, **kwargs) -> Any: ...
def InternetGoOnline(*args, **kwargs) -> Any: ...
def InternetOpen(*args, **kwargs) -> Any: ...
def InternetOpenUrl(*args, **kwargs) -> Any: ...
def InternetQueryOption(*args, **kwargs) -> Any: ...
def InternetReadFile(*args, **kwargs) -> Any: ...
def InternetSetCookie(*args, **kwargs) -> Any: ...
def InternetSetOption(*args, **kwargs) -> Any: ...
def InternetWriteFile(*args, **kwargs) -> Any: ...
def SetUrlCacheEntryGroup(*args, **kwargs) -> Any: ...
def SetUrlCacheGroupAttribute(*args, **kwargs) -> Any: ...
def WinHttpGetDefaultProxyConfiguration(*args, **kwargs) -> Any: ...
def WinHttpGetIEProxyConfigForCurrentUser(*args, **kwargs) -> Any: ...
def WinHttpGetProxyForUrl(*args, **kwargs) -> Any: ...
def WinHttpOpen(*args, **kwargs) -> Any: ...
