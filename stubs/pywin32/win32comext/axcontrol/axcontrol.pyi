from _typeshed import Incomplete
from typing import Any

# from win32.lib.pywintypes import IID  # Crashes stubtest
from typing_extensions import TypeAlias

IID: TypeAlias = Incomplete

EMBDHLP_CREATENOW: int
EMBDHLP_DELAYCREATE: int
EMBDHLP_INPROC_HANDLER: int
EMBDHLP_INPROC_SERVER: int
IID_IObjectWithSite: IID
IID_IOleClientSite: IID
IID_IOleCommandTarget: IID
IID_IOleControl: IID
IID_IOleControlSite: IID
IID_IOleInPlaceActiveObject: IID
IID_IOleInPlaceFrame: IID
IID_IOleInPlaceObject: IID
IID_IOleInPlaceSite: IID
IID_IOleInPlaceSiteEx: IID
IID_IOleInPlaceSiteWindowless: IID
IID_IOleInPlaceUIWindow: IID
IID_IOleLink: IID
IID_IOleObject: IID
IID_ISpecifyPropertyPages: IID
IID_IViewObject: IID
IID_IViewObject2: IID
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

def OleCreate(*args, **kwargs) -> Any: ...
def OleLoadPicture(*args, **kwargs) -> Any: ...
def OleLoadPicturePath(*args, **kwargs) -> Any: ...
def OleSetContainedObject(*args, **kwargs) -> Any: ...
def OleTranslateAccelerator(*args, **kwargs) -> Any: ...
