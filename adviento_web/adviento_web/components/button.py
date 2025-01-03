import reflex as rx
from adviento_web.styles.styles import Color as Color

def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            background_color=Color.ACCENT.value
            # class_name="nes-btn is-error"
        ),
        href=url,
        is_external=True
    )