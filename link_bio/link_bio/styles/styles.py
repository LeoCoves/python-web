import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

#Sizes

class Size(Enum):
    VERY_SMALL = "0.25em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "3em"
    HUGE = "4em"


#Styles

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button : {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
            }
    },
    rx.link : {
        "text_decoration": "none",
        "_hover": {},
        "width": "100%"
    }
}

button_title = {
    "font_size": Size.DEFAULT.value,
    "font_weight": "bold",
    "color": TextColor.HEADER.value
}

button_body = {
    "font_size": Size.DEFAULT.value,
    "color": TextColor.BODY.value
}

title = {
    "width": "100%",
    "font_size": Size.MEDIUM.value,
    "font_weight": "bold",
    "color": TextColor.HEADER.value
}

