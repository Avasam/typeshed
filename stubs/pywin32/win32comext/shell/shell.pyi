from _typeshed import Incomplete
from typing_extensions import TypeAlias

import _win32typing
from win32.lib.pywintypes import IIDType, com_error

error: TypeAlias = com_error  # noqa: Y042

def AssocCreate() -> _win32typing.PyIQueryAssociations: ...
def AssocCreateForClasses() -> _win32typing.PyIUnknown: ...
def DragQueryFile(hglobal: int, index, /) -> str: ...
def DragQueryFileW(hglobal: int, index, /) -> str: ...
def DragQueryPoint(hglobal: int, /) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def IsUserAnAdmin() -> bool: ...
def SHCreateDataObject(
    parent, children: list[Incomplete], do_inner: _win32typing.PyIDataObject, iid: IIDType, /
) -> _win32typing.PyIUnknown: ...
def SHCreateDefaultContextMenu(dcm, iid: IIDType, /) -> _win32typing.PyIUnknown: ...
def SHCreateDefaultExtractIcon() -> _win32typing.PyIDefaultExtractIconInit: ...
def SHCreateShellFolderView(
    sf: _win32typing.PyIShellFolder, viewOuter: _win32typing.PyIShellView | None = ..., callbacks: Incomplete | None = ..., /
) -> _win32typing.PyIShellView: ...
def SHCreateShellItemArray(
    parent: _win32typing.PyIDL, sf: _win32typing.PyIShellFolder, children: list[_win32typing.PyIDL], /
) -> _win32typing.PyIShellItemArray: ...
def SHCreateShellItemArrayFromDataObject(do: _win32typing.PyIDataObject, iid: IIDType, /) -> _win32typing.PyIShellItemArray: ...
def SHCreateShellItemArrayFromShellItem(si: _win32typing.PyIShellItem, riid: IIDType, /) -> _win32typing.PyIShellItemArray: ...
def SHBrowseForFolder(
    hwndOwner: int | None = ...,
    pidlRoot: _win32typing.PyIDL | None = ...,
    title: str | None = ...,
    flags: int = ...,
    callback: Incomplete | None = ...,
    callback_data: Incomplete | None = ...,
    /,
) -> tuple[_win32typing.PyIDL, Incomplete, Incomplete]: ...
def SHGetFileInfo(
    name: _win32typing.PyIDL | str, dwFileAttributes, uFlags, infoAttrs: int = ..., /
) -> tuple[Incomplete, _win32typing.SHFILEINFO]: ...
def SHGetFolderPath(hwndOwner: int, nFolder, handle: int, flags, /) -> str: ...
def SHSetFolderPath(csidl, Path, hToken: int | None = ..., /) -> None: ...
def SHGetFolderLocation(hwndOwner: int, nFolder, hToken: int | None = ..., reserved=..., /) -> _win32typing.PyIDL: ...
def SHGetSpecialFolderPath(hwndOwner: int, nFolder, bCreate: int = ..., /) -> str: ...
def SHGetSpecialFolderLocation(hwndOwner: int, nFolder, /) -> _win32typing.PyIDL: ...
def SHAddToRecentDocs(Flags, data, /) -> None: ...
def SHEmptyRecycleBin(hwnd: int, path: str, flags, /) -> None: ...
def SHQueryRecycleBin(RootPath: str | None = ..., /) -> tuple[Incomplete, Incomplete]: ...
def SHGetDesktopFolder() -> _win32typing.PyIShellFolder: ...
def SHUpdateImage(HashItem: str, Index, Flags, ImageIndex, /) -> None: ...
def SHChangeNotify(EventId, Flags, Item1, Item2, /) -> None: ...
def SHChangeNotifyRegister(hwnd: int, sources, events, msg, /): ...
def SHChangeNotifyDeregister(_id, /) -> None: ...
def SHCreateItemFromParsingName(name, ctx: _win32typing.PyIBindCtx, riid: IIDType, /) -> _win32typing.PyIShellItem: ...
def SHCreateItemFromRelativeName(
    Parent: _win32typing.PyIShellItem, Name, ctx: _win32typing.PyIBindCtx, riid: IIDType, /
) -> _win32typing.PyIShellItem: ...
def SHCreateItemInKnownFolder(FolderId: IIDType, Flags, Name, riid: IIDType, /) -> _win32typing.PyIShellItem: ...
def SHCreateItemWithParent(
    Parent: _win32typing.PyIDL, sfParent: _win32typing.PyIShellFolder, child: _win32typing.PyIDL, riid: IIDType, /
) -> _win32typing.PyIShellItem: ...
def SHGetInstanceExplorer() -> _win32typing.PyIUnknown: ...
def SHFileOperation(operation: _win32typing.SHFILEOPSTRUCT, /) -> tuple[Incomplete, Incomplete]: ...
def StringAsCIDA(pidl: str, /) -> tuple[_win32typing.PyIDL, Incomplete]: ...
def CIDAAsString(pidl: str, /) -> str: ...
def StringAsPIDL(pidl: str, /) -> _win32typing.PyIDL: ...
def AddressAsPIDL(address, /) -> _win32typing.PyIDL: ...
def PIDLAsString(pidl: _win32typing.PyIDL, /) -> str: ...
def SHGetSettings(mask: int = ..., /): ...
def FILEGROUPDESCRIPTORAsString(descriptors: list[Incomplete], arg, /) -> str: ...
def StringAsFILEGROUPDESCRIPTOR(buf, make_unicode: int = ..., /) -> list[Incomplete]: ...
def ShellExecuteEx(
    fMask: int = ...,
    hwnd: int = ...,
    lpVerb: str = ...,
    lpFile: str = ...,
    lpParameters: str = ...,
    lpDirectory: str = ...,
    nShow: int = ...,
    lpIDlist: _win32typing.PyIDL = ...,
    lpClass: str = ...,
    hkeyClass=...,
    dwHotKey=...,
    hIcon: int = ...,
    hMonitor: int = ...,
): ...
def SHGetViewStatePropertyBag(pidl: _win32typing.PyIDL, BagName: str, Flags, riid: IIDType, /) -> _win32typing.PyIPropertyBag: ...
def SHILCreateFromPath(Path: str, Flags, /) -> tuple[_win32typing.PyIDL, Incomplete]: ...
def SHCreateShellItem(
    pidlParent: _win32typing.PyIDL, sfParent: _win32typing.PyIShellFolder, Child: _win32typing.PyIDL, /
) -> _win32typing.PyIShellItem: ...
def SHOpenFolderAndSelectItems(Folder: _win32typing.PyIDL, Items: tuple[_win32typing.PyIDL, ...], Flags=...) -> None: ...
def SHCreateStreamOnFileEx(File, Mode, Attributes, Create, Template: Incomplete | None = ...) -> _win32typing.PyIStream: ...
def SetCurrentProcessExplicitAppUserModelID(AppID: str, /) -> None: ...
def GetCurrentProcessExplicitAppUserModelID() -> str: ...
def SHParseDisplayName(Name, Attributes, BindCtx: _win32typing.PyIBindCtx | None = ...) -> tuple[list[bytes], int]: ...
def SHCreateItemFromIDList(*args): ...  # incomplete
def SHCreateShellItemArrayFromIDLists(*args): ...  # incomplete
def SHGetIDListFromObject(*args): ...  # incomplete
def SHGetNameFromIDList(*args): ...  # incomplete
def SHGetPathFromIDList(*args): ...  # incomplete
def SHGetPathFromIDListW(*args): ...  # incomplete

BHID_AssociationArray: IIDType
BHID_DataObject: IIDType
BHID_EnumItems: IIDType
BHID_Filter: IIDType
BHID_LinkTargetItem: IIDType
BHID_PropertyStore: IIDType
BHID_SFObject: IIDType
BHID_SFUIObject: IIDType
BHID_SFViewObject: IIDType
BHID_Storage: IIDType
BHID_StorageEnum: IIDType
BHID_Stream: IIDType
BHID_ThumbnailHandler: IIDType
BHID_Transfer: IIDType
CGID_DefView: IIDType
CGID_Explorer: IIDType
CGID_ExplorerBarDoc: IIDType
CGID_ShellDocView: IIDType
CGID_ShellServiceObject: IIDType
CLSID_ActiveDesktop: IIDType
CLSID_ApplicationDestinations: IIDType
CLSID_ApplicationDocumentLists: IIDType
CLSID_ControlPanel: IIDType
CLSID_DestinationList: IIDType
CLSID_DragDropHelper: IIDType
CLSID_EnumerableObjectCollection: IIDType
CLSID_FileOperation: IIDType
CLSID_Internet: IIDType
CLSID_InternetShortcut: IIDType
CLSID_KnownFolderManager: IIDType
CLSID_MyComputer: IIDType
CLSID_MyDocuments: IIDType
CLSID_NetworkDomain: IIDType
CLSID_NetworkPlaces: IIDType
CLSID_NetworkServer: IIDType
CLSID_NetworkShare: IIDType
CLSID_Printers: IIDType
CLSID_RecycleBin: IIDType
CLSID_ShellDesktop: IIDType
CLSID_ShellFSFolder: IIDType
CLSID_ShellItem: IIDType
CLSID_ShellLibrary: IIDType
CLSID_ShellLink: IIDType
CLSID_TaskbarList: IIDType
EP_AdvQueryPane: IIDType
EP_Commands: IIDType
EP_Commands_Organize: IIDType
EP_Commands_View: IIDType
EP_DetailsPane: IIDType
EP_NavPane: IIDType
EP_PreviewPane: IIDType
EP_QueryPane: IIDType
FMTID_AudioSummaryInformation: IIDType
FMTID_Briefcase: IIDType
FMTID_Displaced: IIDType
FMTID_ImageProperties: IIDType
FMTID_ImageSummaryInformation: IIDType
FMTID_InternetSite: IIDType
FMTID_Intshcut: IIDType
FMTID_MediaFileSummaryInformation: IIDType
FMTID_Misc: IIDType
FMTID_Query: IIDType
FMTID_ShellDetails: IIDType
FMTID_Storage: IIDType
FMTID_SummaryInformation: IIDType
FMTID_Volume: IIDType
FMTID_WebView: IIDType
FOLDERID_AddNewPrograms: IIDType
FOLDERID_AdminTools: IIDType
FOLDERID_AppUpdates: IIDType
FOLDERID_CDBurning: IIDType
FOLDERID_ChangeRemovePrograms: IIDType
FOLDERID_CommonAdminTools: IIDType
FOLDERID_CommonOEMLinks: IIDType
FOLDERID_CommonPrograms: IIDType
FOLDERID_CommonStartMenu: IIDType
FOLDERID_CommonStartup: IIDType
FOLDERID_CommonTemplates: IIDType
FOLDERID_ComputerFolder: IIDType
FOLDERID_ConflictFolder: IIDType
FOLDERID_ConnectionsFolder: IIDType
FOLDERID_Contacts: IIDType
FOLDERID_ControlPanelFolder: IIDType
FOLDERID_Cookies: IIDType
FOLDERID_Desktop: IIDType
FOLDERID_DeviceMetadataStore: IIDType
FOLDERID_Documents: IIDType
FOLDERID_DocumentsLibrary: IIDType
FOLDERID_Downloads: IIDType
FOLDERID_Favorites: IIDType
FOLDERID_Fonts: IIDType
FOLDERID_GameTasks: IIDType
FOLDERID_Games: IIDType
FOLDERID_History: IIDType
FOLDERID_HomeGroup: IIDType
FOLDERID_ImplicitAppShortcuts: IIDType
FOLDERID_InternetCache: IIDType
FOLDERID_InternetFolder: IIDType
FOLDERID_Libraries: IIDType
FOLDERID_Links: IIDType
FOLDERID_LocalAppData: IIDType
FOLDERID_LocalAppDataLow: IIDType
FOLDERID_LocalizedResourcesDir: IIDType
FOLDERID_Music: IIDType
FOLDERID_MusicLibrary: IIDType
FOLDERID_NetHood: IIDType
FOLDERID_NetworkFolder: IIDType
FOLDERID_OriginalImages: IIDType
FOLDERID_PhotoAlbums: IIDType
FOLDERID_Pictures: IIDType
FOLDERID_PicturesLibrary: IIDType
FOLDERID_Playlists: IIDType
FOLDERID_PrintHood: IIDType
FOLDERID_PrintersFolder: IIDType
FOLDERID_Profile: IIDType
FOLDERID_ProgramData: IIDType
FOLDERID_ProgramFiles: IIDType
FOLDERID_ProgramFilesCommon: IIDType
FOLDERID_ProgramFilesCommonX64: IIDType
FOLDERID_ProgramFilesCommonX86: IIDType
FOLDERID_ProgramFilesX64: IIDType
FOLDERID_ProgramFilesX86: IIDType
FOLDERID_Programs: IIDType
FOLDERID_Public: IIDType
FOLDERID_PublicDesktop: IIDType
FOLDERID_PublicDocuments: IIDType
FOLDERID_PublicDownloads: IIDType
FOLDERID_PublicGameTasks: IIDType
FOLDERID_PublicLibraries: IIDType
FOLDERID_PublicMusic: IIDType
FOLDERID_PublicPictures: IIDType
FOLDERID_PublicRingtones: IIDType
FOLDERID_PublicVideos: IIDType
FOLDERID_QuickLaunch: IIDType
FOLDERID_Recent: IIDType
FOLDERID_RecordedTVLibrary: IIDType
FOLDERID_RecycleBinFolder: IIDType
FOLDERID_ResourceDir: IIDType
FOLDERID_Ringtones: IIDType
FOLDERID_RoamingAppData: IIDType
FOLDERID_SEARCH_CSC: IIDType
FOLDERID_SEARCH_MAPI: IIDType
FOLDERID_SampleMusic: IIDType
FOLDERID_SamplePictures: IIDType
FOLDERID_SamplePlaylists: IIDType
FOLDERID_SampleVideos: IIDType
FOLDERID_SavedGames: IIDType
FOLDERID_SavedSearches: IIDType
FOLDERID_SearchHome: IIDType
FOLDERID_SendTo: IIDType
FOLDERID_SidebarDefaultParts: IIDType
FOLDERID_SidebarParts: IIDType
FOLDERID_StartMenu: IIDType
FOLDERID_Startup: IIDType
FOLDERID_SyncManagerFolder: IIDType
FOLDERID_SyncResultsFolder: IIDType
FOLDERID_SyncSetupFolder: IIDType
FOLDERID_System: IIDType
FOLDERID_SystemX86: IIDType
FOLDERID_Templates: IIDType
FOLDERID_UserPinned: IIDType
FOLDERID_UserProfiles: IIDType
FOLDERID_UserProgramFiles: IIDType
FOLDERID_UserProgramFilesCommon: IIDType
FOLDERID_UsersFiles: IIDType
FOLDERID_UsersLibraries: IIDType
FOLDERID_Videos: IIDType
FOLDERID_VideosLibrary: IIDType
FOLDERID_Windows: IIDType
FOLDERTYPEID_Communications: IIDType
FOLDERTYPEID_CompressedFolder: IIDType
FOLDERTYPEID_Contacts: IIDType
FOLDERTYPEID_ControlPanelCategory: IIDType
FOLDERTYPEID_ControlPanelClassic: IIDType
FOLDERTYPEID_Documents: IIDType
FOLDERTYPEID_Games: IIDType
FOLDERTYPEID_Generic: IIDType
FOLDERTYPEID_GenericLibrary: IIDType
FOLDERTYPEID_GenericSearchResults: IIDType
FOLDERTYPEID_Invalid: IIDType
FOLDERTYPEID_Music: IIDType
FOLDERTYPEID_NetworkExplorer: IIDType
FOLDERTYPEID_OpenSearch: IIDType
FOLDERTYPEID_OtherUsers: IIDType
FOLDERTYPEID_Pictures: IIDType
FOLDERTYPEID_Printers: IIDType
FOLDERTYPEID_PublishedItems: IIDType
FOLDERTYPEID_RecordedTV: IIDType
FOLDERTYPEID_RecycleBin: IIDType
FOLDERTYPEID_SavedGames: IIDType
FOLDERTYPEID_SearchConnector: IIDType
FOLDERTYPEID_SearchHome: IIDType
FOLDERTYPEID_Searches: IIDType
FOLDERTYPEID_SoftwareExplorer: IIDType
FOLDERTYPEID_StartMenu: IIDType
FOLDERTYPEID_UserFiles: IIDType
FOLDERTYPEID_UsersLibraries: IIDType
FOLDERTYPEID_Videos: IIDType
HOTKEYF_ALT: int
HOTKEYF_CONTROL: int
HOTKEYF_EXT: int
HOTKEYF_SHIFT: int
IID_CDefView: IIDType
IID_IADesktopP2: IIDType
IID_IActiveDesktop: IIDType
IID_IActiveDesktopP: IIDType
IID_IApplicationDestinations: IIDType
IID_IApplicationDocumentLists: IIDType
IID_IAsyncOperation: IIDType
IID_IBrowserFrameOptions: IIDType
IID_ICategorizer: IIDType
IID_ICategoryProvider: IIDType
IID_IColumnProvider: IIDType
IID_IContextMenu: IIDType
IID_IContextMenu2: IIDType
IID_IContextMenu3: IIDType
IID_ICopyHook: IIDType
IID_ICopyHookA: IIDType
IID_ICopyHookW: IIDType
IID_ICurrentItem: IIDType
IID_ICustomDestinationList: IIDType
IID_IDefaultExtractIconInit: IIDType
IID_IDeskBand: IIDType
IID_IDisplayItem: IIDType
IID_IDockingWindow: IIDType
IID_IDropTargetHelper: IIDType
IID_IEmptyVolumeCache: IIDType
IID_IEmptyVolumeCache2: IIDType
IID_IEmptyVolumeCacheCallBack: IIDType
IID_IEnumExplorerCommand: IIDType
IID_IEnumIDList: IIDType
IID_IEnumObjects: IIDType
IID_IEnumResources: IIDType
IID_IEnumShellItems: IIDType
IID_IExplorerBrowser: IIDType
IID_IExplorerBrowserEvents: IIDType
IID_IExplorerCommand: IIDType
IID_IExplorerCommandProvider: IIDType
IID_IExplorerPaneVisibility: IIDType
IID_IExtractIcon: IIDType
IID_IExtractIconW: IIDType
IID_IExtractImage: IIDType
IID_IFileOperation: IIDType
IID_IFileOperationProgressSink: IIDType
IID_IIdentityName: IIDType
IID_IKnownFolder: IIDType
IID_IKnownFolderManager: IIDType
IID_INameSpaceTreeControl: IIDType
IID_IObjectArray: IIDType
IID_IObjectCollection: IIDType
IID_IPersistFolder: IIDType
IID_IPersistFolder2: IIDType
IID_IQueryAssociations: IIDType
IID_IRelatedItem: IIDType
IID_IShellBrowser: IIDType
IID_IShellCopyHook: IIDType
IID_IShellCopyHookA: IIDType
IID_IShellCopyHookW: IIDType
IID_IShellExtInit: IIDType
IID_IShellFolder: IIDType
IID_IShellFolder2: IIDType
IID_IShellIcon: IIDType
IID_IShellIconOverlay: IIDType
IID_IShellIconOverlayIdentifier: IIDType
IID_IShellIconOverlayManager: IIDType
IID_IShellItem: IIDType
IID_IShellItem2: IIDType
IID_IShellItemArray: IIDType
IID_IShellItemResources: IIDType
IID_IShellLibrary: IIDType
IID_IShellLink: IIDType
IID_IShellLinkA: IIDType
IID_IShellLinkDataList: IIDType
IID_IShellLinkW: IIDType
IID_IShellView: IIDType
IID_ITaskbarList: IIDType
IID_ITransferAdviseSink: IIDType
IID_ITransferDestination: IIDType
IID_ITransferMediumItem: IIDType
IID_ITransferSource: IIDType
IID_IUniformResourceLocator: IIDType
ResourceTypeStream: IIDType
SID_CtxQueryAssociations: IIDType
SID_DefView: IIDType
SID_LinkSite: IIDType
SID_MenuShellFolder: IIDType
SID_SCommDlgBrowser: IIDType
SID_SGetViewFromViewDual: IIDType
SID_SInternetExplorer: IIDType
SID_SMenuBandBKContextMenu: IIDType
SID_SMenuBandBottom: IIDType
SID_SMenuBandBottomSelected: IIDType
SID_SMenuBandChild: IIDType
SID_SMenuBandContextMenuModifier: IIDType
SID_SMenuBandParent: IIDType
SID_SMenuBandTop: IIDType
SID_SMenuPopup: IIDType
SID_SProgressUI: IIDType
SID_SShellBrowser: IIDType
SID_SShellDesktop: IIDType
SID_STopLevelBrowser: IIDType
SID_STopWindow: IIDType
SID_SUrlHistory: IIDType
SID_SWebBrowserApp: IIDType
SID_ShellFolderViewCB: IIDType
SLGP_RAWPATH: int
SLGP_SHORTPATH: int
SLGP_UNCPRIORITY: int
SLR_ANY_MATCH: int
SLR_INVOKE_MSI: int
SLR_NOLINKINFO: int
SLR_NOSEARCH: int
SLR_NOTRACK: int
SLR_NOUPDATE: int
SLR_NO_UI: int
SLR_UPDATE: int
VID_Details: IIDType
VID_LargeIcons: IIDType
VID_List: IIDType
VID_SmallIcons: IIDType
VID_ThumbStrip: IIDType
VID_Thumbnails: IIDType
VID_Tile: IIDType

def SHGetKnownFolderPath(*args): ...  # incomplete
