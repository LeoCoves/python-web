import reflex as rx
from enum import Enum
from .fonts import Font as Font
from .colors import Text_Color as Text_Color
from .colors import Color as Color


MAX_WIDTH = "1000px"

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
    rx.vstack:{
        "padding": Size.SMALL.value,
        "width": "100%",
    },
    rx.heading:{
        "color": Text_Color.ACCENT.value,
    },
    rx.link: {
        "text_decoration":"none",
        "_hover": {
            "color": Text_Color.ACCENT.value,
            "text_decoration":"none"
        }
    },
    rx.text.span: {
        "font_size": "0.8em"
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BIG.value,
        "color": Text_Color.SECONDARY.value,
        "_hover": {
            "color": Text_Color.PRIMARY.value
        }
    }
}