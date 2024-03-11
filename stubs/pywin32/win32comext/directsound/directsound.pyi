from _typeshed import Incomplete
from typing import ClassVar, NoReturn
from typing_extensions import Never, deprecated

import _win32typing
from win32.lib.pywintypes import IIDType

def DirectSoundCreate(guid: IIDType | None = ..., unk: Incomplete | None = ..., /) -> _win32typing.PyIUnknown: ...
def DirectSoundEnumerate(): ...
def DirectSoundCaptureCreate(guid: IIDType | None = ..., unk: Incomplete | None = ..., /) -> _win32typing.PyIUnknown: ...
def DirectSoundCaptureEnumerate(): ...
def DSCAPS() -> DSCAPSType: ...
def DSBCAPS() -> DSBCAPSType: ...
def DSCCAPS() -> DSCCAPSType: ...
def DSCBCAPS() -> DSCBCAPSType: ...
def DSBUFFERDESC() -> DSBUFFERDESCType: ...
def DSCBUFFERDESC() -> DSCBUFFERDESCType: ...

class DSBCAPSType:
    __name__: ClassVar[str] = "PyDSBCAPS"
    @deprecated("Cannot create 'PyDSBCAPS' instances. Use win32comext.directsound.directsound.DSBCAPS instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwUnlockTransferRate(self) -> int: ...
    @property
    def dwBufferBytes(self): ...
    @property
    def dwPlayCpuOverhead(self): ...

class DSBUFFERDESCType:
    __name__: ClassVar[str] = "PyDSBUFFERDESC"
    @deprecated("Cannot create 'PyDSBUFFERDESC' instances. Use win32comext.directsound.directsound.DSBUFFERDESC instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwBufferBytes(self) -> int: ...
    @property
    def lpwfxFormat(self): ...

class DSCAPSType:  # aka PyDSCAPS
    __name__: ClassVar[str] = "PyDSCAPSType"
    @deprecated("Cannot create 'PyDSCAPSType' instances. Use win32comext.directsound.directsound.DSCAPS instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwMinSecondarySampleRate(self) -> int: ...
    @property
    def dwMaxSecondarySampleRate(self) -> int: ...
    @property
    def dwPrimaryBuffers(self) -> int: ...
    @property
    def dwMaxHwMixingAllBuffers(self) -> int: ...
    @property
    def dwMaxHwMixingStaticBuffers(self) -> int: ...
    @property
    def dwMaxHwMixingStreamingBuffers(self) -> int: ...
    @property
    def dwFreeHwMixingAllBuffers(self) -> int: ...
    @property
    def dwFreeHwMixingStaticBuffers(self) -> int: ...
    @property
    def dwFreeHwMixingStreamingBuffers(self) -> int: ...
    @property
    def dwMaxHw3DAllBuffers(self) -> int: ...
    @property
    def dwMaxHw3DStaticBuffers(self) -> int: ...
    @property
    def dwMaxHw3DStreamingBuffers(self) -> int: ...
    @property
    def dwFreeHw3DAllBuffers(self) -> int: ...
    @property
    def dwFreeHw3DStaticBuffers(self) -> int: ...
    @property
    def dwFreeHw3DStreamingBuffers(self) -> int: ...
    @property
    def dwTotalHwMemBytes(self) -> int: ...
    @property
    def dwFreeHwMemBytes(self) -> int: ...
    @property
    def dwMaxContigFreeHwMemBytes(self) -> int: ...
    @property
    def dwUnlockTransferRateHwBuffers(self) -> int: ...
    @property
    def dwPlayCpuOverheadSwBuffers(self) -> int: ...

class DSCBCAPSType:
    __name__: ClassVar[str] = "PyDSCBCAPSType"
    @deprecated("Cannot create 'PyDSCBCAPSType' instances. Use win32comext.directsound.directsound.DSCBCAPS instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwBufferBytes(self) -> int: ...

class DSCBUFFERDESCType:
    __name__: ClassVar[str] = "PyDSCBUFFERDESC"
    @deprecated("Cannot create 'PyDSCBUFFERDESC' instances. Use win32comext.directsound.directsound.DSCBUFFERDESC instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwBufferBytes(self) -> int: ...
    @property
    def lpwfxFormat(self): ...

class DSCCAPSType:
    __name__: ClassVar[str] = "PyDSCCAPSType"
    @deprecated("Cannot create 'PyDSCCAPSType' instances. Use win32comext.directsound.directsound.DSCCAPS instead.")
    def __init__(self, *args: Never, **kwargs: Never) -> NoReturn: ...
    @property
    def dwFlags(self) -> int: ...
    @property
    def dwFormats(self) -> int: ...
    @property
    def dwChannels(self) -> int: ...

DS3DMODE_DISABLE: int
DS3DMODE_HEADRELATIVE: int
DS3DMODE_NORMAL: int
DSBCAPS_CTRL3D: int
DSBCAPS_CTRLFREQUENCY: int
DSBCAPS_CTRLPAN: int
DSBCAPS_CTRLPOSITIONNOTIFY: int
DSBCAPS_CTRLVOLUME: int
DSBCAPS_GETCURRENTPOSITION2: int
DSBCAPS_GLOBALFOCUS: int
DSBCAPS_LOCHARDWARE: int
DSBCAPS_LOCSOFTWARE: int
DSBCAPS_MUTE3DATMAXDISTANCE: int
DSBCAPS_PRIMARYBUFFER: int
DSBCAPS_STATIC: int
DSBCAPS_STICKYFOCUS: int
DSBLOCK_ENTIREBUFFER: int
DSBLOCK_FROMWRITECURSOR: int
DSBPLAY_LOOPING: int
DSBSTATUS_BUFFERLOST: int
DSBSTATUS_LOOPING: int
DSBSTATUS_PLAYING: int
DSCAPS_CERTIFIED: int
DSCAPS_CONTINUOUSRATE: int
DSCAPS_EMULDRIVER: int
DSCAPS_PRIMARY16BIT: int
DSCAPS_PRIMARY8BIT: int
DSCAPS_PRIMARYMONO: int
DSCAPS_PRIMARYSTEREO: int
DSCAPS_SECONDARY16BIT: int
DSCAPS_SECONDARY8BIT: int
DSCAPS_SECONDARYMONO: int
DSCAPS_SECONDARYSTEREO: int
DSCBCAPS_WAVEMAPPED: int
DSCCAPS_EMULDRIVER: int
DSSCL_EXCLUSIVE: int
DSSCL_NORMAL: int
DSSCL_PRIORITY: int
DSSCL_WRITEPRIMARY: int
DSSPEAKER_GEOMETRY_MAX: int
DSSPEAKER_GEOMETRY_MIN: int
DSSPEAKER_GEOMETRY_NARROW: int
DSSPEAKER_GEOMETRY_WIDE: int
DSSPEAKER_HEADPHONE: int
DSSPEAKER_MONO: int
DSSPEAKER_QUAD: int
DSSPEAKER_STEREO: int
DSSPEAKER_SURROUND: int
DSBFREQUENCY_MAX: int
DSBFREQUENCY_MIN: int
DSBFREQUENCY_ORIGINAL: int
DSBPAN_CENTER: int
DSBPAN_LEFT: int
DSBPAN_RIGHT: int
DSBPN_OFFSETSTOP: int
DSBSIZE_MAX: int
DSBSIZE_MIN: int
DSBVOLUME_MAX: int
DSBVOLUME_MIN: int
DSCBLOCK_ENTIREBUFFER: int
DSCBSTART_LOOPING: int
DSCBSTATUS_CAPTURING: int
DSCBSTATUS_LOOPING: int
DSERR_ACCESSDENIED: int
DSERR_ALLOCATED: int
DSERR_ALREADYINITIALIZED: int
DSERR_BADFORMAT: int
DSERR_BADSENDBUFFERGUID: int
DSERR_BUFFERLOST: int
DSERR_BUFFERTOOSMALL: int
DSERR_CONTROLUNAVAIL: int
DSERR_DS8_REQUIRED: int
DSERR_FXUNAVAILABLE: int
DSERR_GENERIC: int
DSERR_INVALIDCALL: int
DSERR_INVALIDPARAM: int
DSERR_NOAGGREGATION: int
DSERR_NODRIVER: int
DSERR_NOINTERFACE: int
DSERR_OBJECTNOTFOUND: int
DSERR_OTHERAPPHASPRIO: int
DSERR_OUTOFMEMORY: int
DSERR_PRIOLEVELNEEDED: int
DSERR_SENDLOOP: int
DSERR_UNINITIALIZED: int
DSERR_UNSUPPORTED: int
DS_NO_VIRTUALIZATION: int
DS_OK: int
IID_IDirectSound: IIDType
IID_IDirectSoundBuffer: IIDType
IID_IDirectSoundCapture: IIDType
IID_IDirectSoundCaptureBuffer: IIDType
IID_IDirectSoundNotify: IIDType
