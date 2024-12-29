import reflex as rx
from enum import Enum

#Sizes

class Size(Enum):
    VERY_SMALL = "0.25em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "3em"
    HUGE = "4em"

#Colors

class Color(Enum):
    PRIMARY = "blue"
    SECONDARY = "green"
    TERTIARY = "red"

#Styles

BASE_STYLE = {
    rx.button : {
        "width": "100%",
        "height": "100%",
    }
}


