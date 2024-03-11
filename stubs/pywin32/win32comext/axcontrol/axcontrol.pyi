import _win32typing
from win32.lib.pywintypes import IIDType

def OleCreate(
    clsid,
    clsid1,
    obCLSID: IIDType,
    obIID: IIDType,
    renderopt,
    obFormatEtc,
    obOleClientSite: _win32typing.PyIOleClientSite,
    obStorage: _win32typing.PyIStorage,
    /,
) -> _win32typing.PyIOleObject: ...
def OleLoadPicture(stream: _win32typing.PyIStream, size, runMode, arg: IIDType, arg1: IIDType, /) -> _win32typing.PyIUnknown: ...
def OleLoadPicturePath(url_or_path: str, unk, reserved, clr, arg: IIDType, arg1: IIDType, /) -> _win32typing.PyIUnknown: ...
def OleSetContainedObject(unk: _win32typing.PyIUnknown, fContained, /) -> None: ...
def OleTranslateAccelerator(frame: _win32typing.PyIOleInPlaceFrame, frame_info, msg: _win32typing.PyMSG, /) -> None: ...

EMBDHLP_CREATENOW: int
EMBDHLP_DELAYCREATE: int
EMBDHLP_INPROC_HANDLER: int
EMBDHLP_INPROC_SERVER: int
OLECLOSE_NOSAVE: int
OLECLOSE_PROMPTSAVE: int
OLECLOSE_SAVEIFDIRTY: int
OLECMDF_ENABLED: int
OLECMDF_LATCHED: int
OLECMDF_NINCHED: int
OLECMDF_SUPPORTED: int
OLECMDTEXTF_NAME: int
OLECMDTEXTF_NONE: int
OLECMDTEXTF_STATUS: int
OLECREATE_LEAVERUNNING: int
OLEIVERB_DISCARDUNDOSTATE: int
OLEIVERB_HIDE: int
OLEIVERB_INPLACEACTIVATE: int
OLEIVERB_OPEN: int
OLEIVERB_PRIMARY: int
OLEIVERB_SHOW: int
OLEIVERB_UIACTIVATE: int
IID_IObjectWithSite: IIDType
IID_IOleClientSite: IIDType
IID_IOleCommandTarget: IIDType
IID_IOleControl: IIDType
IID_IOleControlSite: IIDType
IID_IOleInPlaceActiveObject: IIDType
IID_IOleInPlaceFrame: IIDType
IID_IOleInPlaceObject: IIDType
IID_IOleInPlaceSite: IIDType
IID_IOleInPlaceSiteEx: IIDType
IID_IOleInPlaceSiteWindowless: IIDType
IID_IOleInPlaceUIWindow: IIDType
IID_IOleLink: IIDType
IID_IOleObject: IIDType
IID_ISpecifyPropertyPages: IIDType
IID_IViewObject: IIDType
IID_IViewObject2: IIDType
