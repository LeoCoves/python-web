import reflex as rx
from adviento_web.styles.styles import Size as Size
from adviento_web.styles.styles import Text_Color as Text_Color

def header_text(icon: str, text: str, dark: bool) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-large {icon}",
        ),
        rx.heading(
            text,
            size="4",
            padding_left=Size.DEFAULT.value,
            align_self="center",
            color=Text_Color.ACCENT.value if dark else Text_Color.PRIMARY.value
        ),
        width="100%",
        padding_bottom=Size.DEFAULT.value
    )