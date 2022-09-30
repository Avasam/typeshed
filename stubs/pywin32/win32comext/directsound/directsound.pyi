from _typeshed import Incomplete
from typing import Any

# from win32.lib.pywintypes import IID  # Crashes stubtest
from typing_extensions import TypeAlias

IID: TypeAlias = Incomplete

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
DSBFREQUENCY_MAX: int
DSBFREQUENCY_MIN: int
DSBFREQUENCY_ORIGINAL: int
DSBLOCK_ENTIREBUFFER: int
DSBLOCK_FROMWRITECURSOR: int
DSBPAN_CENTER: int
DSBPAN_LEFT: int
DSBPAN_RIGHT: int
DSBPLAY_LOOPING: int
DSBPN_OFFSETSTOP: int
DSBSIZE_MAX: int
DSBSIZE_MIN: int
DSBSTATUS_BUFFERLOST: int
DSBSTATUS_LOOPING: int
DSBSTATUS_PLAYING: int
DSBVOLUME_MAX: int
DSBVOLUME_MIN: int
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
DSCBLOCK_ENTIREBUFFER: int
DSCBSTART_LOOPING: int
DSCBSTATUS_CAPTURING: int
DSCBSTATUS_LOOPING: int
DSCCAPS_EMULDRIVER: int
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
DS_NO_VIRTUALIZATION: int
DS_OK: int
IID_IDirectSound: IID
IID_IDirectSoundBuffer: IID
IID_IDirectSoundCapture: IID
IID_IDirectSoundCaptureBuffer: IID
IID_IDirectSoundNotify: IID

class DSBCAPSType:
    dwBufferBytes: Any
    dwFlags: Any
    dwPlayCpuOverhead: Any
    dwUnlockTransferRate: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class DSBUFFERDESCType:
    dwBufferBytes: Any
    dwFlags: Any
    lpwfxFormat: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class DSCAPSType:
    dwFlags: Any
    dwFreeHw3DAllBuffers: Any
    dwFreeHw3DStaticBuffers: Any
    dwFreeHw3DStreamingBuffers: Any
    dwFreeHwMemBytes: Any
    dwFreeHwMixingAllBuffers: Any
    dwFreeHwMixingStaticBuffers: Any
    dwFreeHwMixingStreamingBuffers: Any
    dwMaxContigFreeHwMemBytes: Any
    dwMaxHw3DAllBuffers: Any
    dwMaxHw3DStaticBuffers: Any
    dwMaxHw3DStreamingBuffers: Any
    dwMaxHwMixingAllBuffers: Any
    dwMaxHwMixingStaticBuffers: Any
    dwMaxHwMixingStreamingBuffers: Any
    dwMaxSecondarySampleRate: Any
    dwMinSecondarySampleRate: Any
    dwPlayCpuOverheadSwBuffers: Any
    dwPrimaryBuffers: Any
    dwTotalHwMemBytes: Any
    dwUnlockTransferRateHwBuffers: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class DSCBCAPSType:
    dwBufferBytes: Any
    dwFlags: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class DSCBUFFERDESCType:
    dwBufferBytes: Any
    dwFlags: Any
    lpwfxFormat: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class DSCCAPSType:
    dwChannels: Any
    dwFlags: Any
    dwFormats: Any
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

def DSBCAPS(*args, **kwargs) -> Any: ...
def DSBUFFERDESC(*args, **kwargs) -> Any: ...
def DSCAPS(*args, **kwargs) -> Any: ...
def DSCBCAPS(*args, **kwargs) -> Any: ...
def DSCBUFFERDESC(*args, **kwargs) -> Any: ...
def DSCCAPS(*args, **kwargs) -> Any: ...
def DirectSoundCaptureCreate(*args, **kwargs) -> Any: ...
def DirectSoundCaptureEnumerate(*args, **kwargs) -> Any: ...
def DirectSoundCreate(*args, **kwargs) -> Any: ...
def DirectSoundEnumerate(*args, **kwargs) -> Any: ...
