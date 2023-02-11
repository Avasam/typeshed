from typing_extensions import Final

from win32.lib.pywintypes import error as error

def set_timer(Elapse, TimerFunc): ...
def kill_timer(timer_id): ...

__version__: Final[bytes]
