from collections.abc import Callable, Iterable, Sequence
from types import FunctionType, MethodType
from typing import Any, Pattern, overload
from typing_extensions import Literal, TypeAlias, TypedDict

from Xlib import error
from Xlib._typing import ErrorHandler
from Xlib.protocol import display, request, rq
from Xlib.xobject import colormap, cursor, drawable, fontable, resource

_ResourceBaseClass: TypeAlias = (
    resource.Resource
    | drawable.Drawable
    | drawable.Window
    | drawable.Pixmap
    | fontable.Fontable
    | fontable.Font
    | fontable.GC
    | colormap.Colormap
    | cursor.Cursor
)

# Is the type of the `_resource_baseclasses` variable, defined in this file at runtime
class _ResourceBaseClassesType(TypedDict):  # noqa: Y049
    resource: type[resource.Resource]
    drawable: type[drawable.Drawable]
    window: type[drawable.Window]
    pixmap: type[drawable.Pixmap]
    fontable: type[fontable.Fontable]
    font: type[fontable.Font]
    gc: type[fontable.GC]
    colormap: type[colormap.Colormap]
    cursor: type[cursor.Cursor]

class _BaseDisplay(display.Display):
    def __init__(self, display: str | None = ...) -> None: ...
    def get_atom(self, atomname: str, only_if_exists: bool = ...) -> int: ...

class Display:
    display: _BaseDisplay
    keysym_translations: dict[int, str]
    extensions: list[str]
    class_extension_dicts: dict[str, dict[str, FunctionType]]
    display_extension_methods: dict[str, Callable]
    extension_event: rq.DictWrapper
    def __init__(self, display: str | None = ...) -> None: ...
    def get_display_name(self) -> str: ...
    def fileno(self) -> int: ...
    def close(self) -> None: ...
    def set_error_handler(self, handler: ErrorHandler[object] | None) -> None: ...
    def flush(self) -> None: ...
    def sync(self) -> None: ...
    def next_event(self) -> rq.Event: ...
    def pending_events(self) -> int: ...
    def has_extension(self, extension: str) -> bool: ...
    @overload
    def create_resource_object(self, type: Literal["resource"], id: int) -> resource.Resource: ...
    @overload
    def create_resource_object(self, type: Literal["drawable"], id: int) -> drawable.Drawable: ...
    @overload
    def create_resource_object(self, type: Literal["window"], id: int) -> drawable.Window: ...
    @overload
    def create_resource_object(self, type: Literal["pixmap"], id: int) -> drawable.Pixmap: ...
    @overload
    def create_resource_object(self, type: Literal["fontable"], id: int) -> fontable.Fontable: ...
    @overload
    def create_resource_object(self, type: Literal["font"], id: int) -> fontable.Font: ...
    @overload
    def create_resource_object(self, type: Literal["gc"], id: int) -> fontable.GC: ...
    @overload
    def create_resource_object(self, type: Literal["colormap"], id: int) -> colormap.Colormap: ...
    @overload
    def create_resource_object(self, type: Literal["cursor"], id: int) -> cursor.Cursor: ...
    @overload
    def create_resource_object(self, type: str, id: int) -> resource.Resource: ...
    def __getattr__(self, attr: str) -> MethodType: ...
    def screen(self, sno: int | None = ...) -> rq.Struct: ...
    def screen_count(self) -> int: ...
    def get_default_screen(self) -> int: ...
    def extension_add_method(self, object: str, name: str, function: Callable) -> None: ...
    def extension_add_event(self, code: int, evt: type, name: str | None = ...) -> None: ...
    def extension_add_subevent(self, code: int, subcode: int | None, evt: type[rq.Event], name: str | None = ...) -> None: ...
    def extension_add_error(self, code: int, err: type[error.XError]) -> None: ...
    def keycode_to_keysym(self, keycode: int, index: int) -> int: ...
    def keysym_to_keycode(self, keysym: int) -> int: ...
    def keysym_to_keycodes(self, keysym: int) -> Iterable[tuple[int, int]]: ...
    def refresh_keyboard_mapping(self, evt: rq.Event) -> None: ...
    def lookup_string(self, keysym: int) -> str | None: ...
    def rebind_string(self, keysym: int, newstring: str | None) -> None: ...
    def intern_atom(self, name: str, only_if_exists: bool = ...) -> int: ...
    def get_atom(self, atom: str, only_if_exists: bool = ...) -> int: ...
    def get_atom_name(self, atom: int) -> str: ...
    def get_selection_owner(self, selection: int) -> int: ...
    def send_event(
        self,
        destination: int,
        event: rq.Event,
        event_mask: int = ...,
        propagate: bool = ...,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def ungrab_pointer(self, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def change_active_pointer_grab(
        self, event_mask: int, cursor: cursor.Cursor, time: int, onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def ungrab_keyboard(self, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def allow_events(self, mode: int, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def grab_server(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def ungrab_server(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def warp_pointer(
        self,
        x: int,
        y: int,
        src_window: int = ...,
        src_x: int = ...,
        src_y: int = ...,
        src_width: int = ...,
        src_height: int = ...,
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def set_input_focus(self, focus: int, revert_to: int, time: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_input_focus(self) -> request.GetInputFocus: ...
    def query_keymap(self) -> bytes: ...  # TODO: Validate if this is correct
    def open_font(self, name: str) -> _ResourceBaseClass | None: ...
    def list_fonts(self, pattern: Pattern[str] | str, max_names: int) -> list[str]: ...
    def list_fonts_with_info(self, pattern: Pattern[str] | str, max_names: int) -> request.ListFontsWithInfo: ...
    def set_font_path(self, path: Sequence[str], onerror: ErrorHandler[object] | None = ...) -> None: ...
    def get_font_path(self) -> list[str]: ...
    def query_extension(self, name: str) -> request.QueryExtension | None: ...
    def list_extensions(self) -> list[str]: ...
    def change_keyboard_mapping(
        self, first_keycode: int, keysyms: Sequence[Sequence[int]], onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def get_keyboard_mapping(self, first_keycode: int, count: int) -> list[tuple[int, ...]]: ...
    def change_keyboard_control(self, onerror: ErrorHandler[object] | None = ..., **keys: object) -> None: ...
    def get_keyboard_control(self) -> request.GetKeyboardControl: ...
    def bell(self, percent: int = ..., onerror: ErrorHandler[object] | None = ...) -> None: ...
    def change_pointer_control(
        self, accel: tuple[int, int] | None = ..., threshold: int | None = ..., onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def get_pointer_control(self) -> request.GetPointerControl: ...
    def set_screen_saver(
        self, timeout: int, interval: int, prefer_blank: int, allow_exposures: int, onerror: ErrorHandler[object] | None = ...
    ) -> None: ...
    def get_screen_saver(self) -> request.GetScreenSaver: ...
    def change_hosts(
        self,
        mode: int,
        host_family: int,
        host: Sequence[int] | Sequence[bytes],  # TODO: validate
        onerror: ErrorHandler[object] | None = ...,
    ) -> None: ...
    def list_hosts(self) -> request.ListHosts: ...
    def set_access_control(self, mode: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def set_close_down_mode(self, mode: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def force_screen_saver(self, mode: int, onerror: ErrorHandler[object] | None = ...) -> None: ...
    def set_pointer_mapping(self, map: Sequence[int]) -> int: ...
    def get_pointer_mapping(self) -> list[int]: ...
    def set_modifier_mapping(self, keycodes: rq._ModifierMappingList8Elements) -> int: ...
    def get_modifier_mapping(self) -> Sequence[Sequence[int]]: ...
    def no_operation(self, onerror: ErrorHandler[object] | None = ...) -> None: ...
