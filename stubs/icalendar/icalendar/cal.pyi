import datetime
from _typeshed import Incomplete, SupportsItems
from collections.abc import Callable
from typing import Any, ClassVar, Final, Literal, NamedTuple, overload
from typing_extensions import Self

from .alarms import Alarms
from .caselessdict import CaselessDict
from .parser import Contentline, Contentlines
from .prop import TypesFactory
from .timezone.tzp import TZP

__all__ = [
    "INLINE",
    "Alarm",
    "Calendar",
    "Component",
    "ComponentFactory",
    "Event",
    "FreeBusy",
    "IncompleteComponent",
    "InvalidCalendar",
    "Journal",
    "Timezone",
    "TimezoneDaylight",
    "TimezoneStandard",
    "Todo",
    "component_factory",
    "get_example",
]

def get_example(component_directory: str, example_name: str) -> bytes: ...

class ComponentFactory(CaselessDict[Incomplete]):
    def __init__(self, *args, **kwargs) -> None: ...

INLINE: CaselessDict[int]

class InvalidCalendar(ValueError): ...
class IncompleteComponent(ValueError): ...

def create_utc_property(name: str, docs: str) -> property: ...

class Component(CaselessDict[Incomplete]):
    name: ClassVar[str | None]
    required: ClassVar[tuple[str, ...]]
    singletons: ClassVar[tuple[str, ...]]
    multiple: ClassVar[tuple[str, ...]]
    exclusive: ClassVar[tuple[str, ...]]
    inclusive: ClassVar[tuple[tuple[str, ...], ...]]
    ignore_exceptions: ClassVar[bool]
    subcomponents: list[Incomplete]
    errors: list[str]

    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def is_empty(self) -> bool: ...
    @overload
    def add(self, name: str, value: Any, *, encode: Literal[False]) -> None: ...
    @overload
    def add(self, name: str, value: Any, parameters: None, encode: Literal[False]) -> None: ...
    @overload
    def add(
        self, name: str, value: Any, parameters: SupportsItems[str, str | None] | None = None, encode: Literal[True] = True
    ) -> None: ...
    def decoded(self, name, default=[]): ...
    def get_inline(self, name, decode: bool = True): ...
    def set_inline(self, name, values, encode: bool = True) -> None: ...
    def add_component(self, component: Component) -> None: ...
    def walk(self, name: str | None = None, select: Callable[[Component], bool] = ...) -> list[Component]: ...
    def property_items(self, recursive: bool = True, sorted: bool = True) -> list[tuple[str, object]]: ...
    @overload
    @classmethod
    def from_ical(cls, st: str, multiple: Literal[False] = False) -> Component: ...  # or any of its subclasses
    @overload
    @classmethod
    def from_ical(cls, st: str, multiple: Literal[True]) -> list[Component]: ...  # or any of its subclasses
    def content_line(self, name: str, value, sorted: bool = True) -> Contentline: ...
    def content_lines(self, sorted: bool = True) -> Contentlines: ...
    def to_ical(self, sorted: bool = True) -> bytes: ...
    def __eq__(self, other: Component) -> bool: ...  # type: ignore[override]
    @property
    def DTSTAMP(self) -> datetime.datetime | None: ...
    @DTSTAMP.setter
    def DTSTAMP(self, value: datetime.datetime) -> None: ...
    @property
    def LAST_MODIFIED(self) -> datetime.datetime | None: ...
    @LAST_MODIFIED.setter
    def LAST_MODIFIED(self, value: datetime.datetime) -> None: ...
    def is_thunderbird(self) -> bool: ...

# type_def is a TypeForm
def create_single_property(
    prop: str, value_attr: str | None, value_type: tuple[type, ...], type_def: Any, doc: str, vProp: type[Incomplete] = ...
) -> property: ...

class Event(Component):
    name: ClassVar[Literal["VEVENT"]]
    @property
    def alarms(self) -> Alarms: ...
    @classmethod
    def example(cls, name: str = "rfc_9074_example_3") -> Event: ...
    @property
    def DTSTART(self) -> datetime.date | datetime.datetime | None: ...
    @DTSTART.setter
    def DTSTART(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def DTEND(self) -> datetime.date | datetime.datetime | None: ...
    @DTEND.setter
    def DTEND(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def DURATION(self) -> datetime.timedelta | None: ...
    @DURATION.setter
    def DURATION(self, value: datetime.timedelta | None) -> None: ...
    @property
    def duration(self) -> datetime.timedelta: ...
    @property
    def start(self) -> datetime.date | datetime.datetime: ...
    @start.setter
    def start(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def end(self) -> datetime.date | datetime.datetime: ...
    @end.setter
    def end(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def X_MOZ_SNOOZE_TIME(self) -> datetime.datetime | None: ...
    @X_MOZ_SNOOZE_TIME.setter
    def X_MOZ_SNOOZE_TIME(self, value: datetime.datetime) -> None: ...
    @property
    def X_MOZ_LASTACK(self) -> datetime.datetime | None: ...
    @X_MOZ_LASTACK.setter
    def X_MOZ_LASTACK(self, value: datetime.datetime) -> None: ...

class Todo(Component):
    name: ClassVar[Literal["VTODO"]]
    @property
    def DTSTART(self) -> datetime.datetime | datetime.date | None: ...
    @DTSTART.setter
    def DTSTART(self, value: datetime.datetime | datetime.date | None) -> None: ...
    @property
    def DUE(self) -> datetime.datetime | datetime.date | None: ...
    @DUE.setter
    def DUE(self, value: datetime.datetime | datetime.date | None) -> None: ...
    @property
    def DURATION(self) -> datetime.timedelta | None: ...
    @DURATION.setter
    def DURATION(self, value: datetime.timedelta | None) -> None: ...
    @property
    def start(self) -> datetime.datetime | datetime.date: ...
    @start.setter
    def start(self, value: datetime.datetime | datetime.date | None) -> None: ...
    @property
    def end(self) -> datetime.datetime | datetime.date: ...
    @end.setter
    def end(self, value: datetime.datetime | datetime.date | None) -> None: ...
    @property
    def duration(self) -> datetime.timedelta: ...
    @property
    def X_MOZ_SNOOZE_TIME(self) -> datetime.datetime | None: ...
    @X_MOZ_SNOOZE_TIME.setter
    def X_MOZ_SNOOZE_TIME(self, value: datetime.datetime) -> None: ...
    @property
    def X_MOZ_LASTACK(self) -> datetime.datetime | None: ...
    @X_MOZ_LASTACK.setter
    def X_MOZ_LASTACK(self, value: datetime.datetime) -> None: ...
    @property
    def alarms(self) -> Alarms: ...

class Journal(Component):
    name: ClassVar[Literal["VJOURNAL"]]
    @property
    def DTSTART(self) -> datetime.date | datetime.datetime | None: ...
    @DTSTART.setter
    def DTSTART(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def start(self) -> datetime.date | datetime.datetime: ...
    @start.setter
    def start(self, value: datetime.date | datetime.datetime | None) -> None: ...
    end = start
    @property
    def duration(self) -> datetime.timedelta: ...

class FreeBusy(Component):
    name: ClassVar[Literal["VFREEBUSY"]]

class Timezone(Component):
    name: ClassVar[Literal["VTIMEZONE"]]
    @classmethod
    def example(cls, name: str = "pacific_fiji") -> Calendar: ...
    def to_tz(self, tzp: TZP = ..., lookup_tzid: bool = True) -> datetime.tzinfo: ...
    @property
    def tz_name(self) -> str: ...
    def get_transitions(self) -> tuple[list[datetime.datetime], list[tuple[datetime.timedelta, datetime.timedelta, str]]]: ...
    @classmethod
    def from_tzinfo(
        cls, timezone: datetime.tzinfo, tzid: str | None = None, first_date: datetime.date = ..., last_date: datetime.date = ...
    ) -> Self: ...
    @classmethod
    def from_tzid(cls, tzid: str, tzp: TZP = ..., first_date: datetime.date = ..., last_date: datetime.date = ...) -> Self: ...
    @property
    def standard(self) -> list[TimezoneStandard]: ...
    @property
    def daylight(self) -> list[TimezoneDaylight]: ...

class TimezoneStandard(Component):
    name: ClassVar[Literal["STANDARD"]]
    @property
    def DTSTART(self) -> datetime.date | datetime.datetime | None: ...
    @DTSTART.setter
    def DTSTART(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def TZOFFSETTO(self) -> datetime.timedelta | None: ...
    @TZOFFSETTO.setter
    def TZOFFSETTO(self, value: datetime.timedelta | None) -> None: ...
    @property
    def TZOFFSETFROM(self) -> datetime.timedelta | None: ...
    @TZOFFSETFROM.setter
    def TZOFFSETFROM(self, value: datetime.timedelta | None) -> None: ...

class TimezoneDaylight(Component):
    name: ClassVar[Literal["DAYLIGHT"]]
    @property
    def DTSTART(self) -> datetime.date | datetime.datetime | None: ...
    @DTSTART.setter
    def DTSTART(self, value: datetime.date | datetime.datetime | None) -> None: ...
    @property
    def TZOFFSETTO(self) -> datetime.timedelta | None: ...
    @TZOFFSETTO.setter
    def TZOFFSETTO(self, value: datetime.timedelta | None) -> None: ...
    @property
    def TZOFFSETFROM(self) -> datetime.timedelta | None: ...
    @TZOFFSETFROM.setter
    def TZOFFSETFROM(self, value: datetime.timedelta | None) -> None: ...

class Alarm(Component):
    name: ClassVar[Literal["VALARM"]]
    @property
    def REPEAT(self) -> int: ...
    @REPEAT.setter
    def REPEAT(self, value: int) -> None: ...
    @property
    def DURATION(self) -> datetime.timedelta | None: ...
    @DURATION.setter
    def DURATION(self, value: datetime.timedelta | None) -> None: ...
    @property
    def ACKNOWLEDGED(self) -> datetime.datetime | None: ...
    @ACKNOWLEDGED.setter
    def ACKNOWLEDGED(self, value: datetime.datetime | None) -> None: ...
    @property
    def TRIGGER(self) -> datetime.timedelta | datetime.datetime | None: ...
    @TRIGGER.setter
    def TRIGGER(self, value: datetime.timedelta | datetime.datetime | None) -> None: ...
    @property
    def TRIGGER_RELATED(self) -> Literal["START", "END"]: ...
    @TRIGGER_RELATED.setter
    def TRIGGER_RELATED(self, value: Literal["START", "END"]) -> None: ...

    class Triggers(NamedTuple):
        start: tuple[datetime.timedelta, ...]
        end: tuple[datetime.timedelta, ...]
        absolute: tuple[datetime.datetime, ...]

    @property
    def triggers(self) -> Alarm.Triggers: ...

class Calendar(Component):
    name: ClassVar[Literal["VCALENDAR"]]
    @classmethod
    def example(cls, name: str = "example") -> Calendar: ...
    @property
    def events(self) -> list[Event]: ...
    @property
    def todos(self) -> list[Todo]: ...
    def get_used_tzids(self) -> set[str]: ...
    def get_missing_tzids(self) -> set[str]: ...
    @property
    def timezones(self) -> list[Timezone]: ...
    def add_missing_timezones(self, first_date: datetime.date = ..., last_date: datetime.date = ...) -> None: ...

types_factory: Final[TypesFactory]
component_factory: Final[ComponentFactory]
