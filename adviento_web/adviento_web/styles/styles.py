import reflex as rx
from enum import Enum
from .fonts import Font as Font
from .colors import Text_Color as Text_Color
from .colors import Color as Color


class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color" : Text_Color.PRIMARY.value,
    "background_color": Color.PRIMARY.value,
}