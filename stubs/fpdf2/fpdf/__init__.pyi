from pathlib import Path
from typing_extensions import Final

from .enums import Align as Align, XPos as XPos, YPos as YPos
from .fpdf import FPDF as FPDF, FPDF_FONT_DIR as FPDF_FONT_DIR, FPDF_VERSION as FPDF_VERSION, TitleStyle as TitleStyle
from .html import HTML2FPDF as HTML2FPDF, HTMLMixin as HTMLMixin
from .prefs import ViewerPreferences as ViewerPreferences
from .template import FlexTemplate as FlexTemplate, Template as Template

__license__: Final[str]
__version__: Final[Path]

__all__ = [
    "__version__",
    "__license__",
    "FPDF",
    "Align",
    "XPos",
    "YPos",
    "Template",
    "FlexTemplate",
    "TitleStyle",
    "ViewerPreferences",
    "HTMLMixin",
    "HTML2FPDF",
    "FPDF_VERSION",
    "FPDF_FONT_DIR",
]
