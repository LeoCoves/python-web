import reflex as rx
from adviento_web.styles.styles import Size as Size

def header_text(icon: str, text: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-large {icon}",
        ),
        rx.heading(
            text,
            size="4",
            padding_left=Size.DEFAULT.value,
            align_self="center"
        ),
        width="100%",
        padding_bottom=Size.DEFAULT.value
    )