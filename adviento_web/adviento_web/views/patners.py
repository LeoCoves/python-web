import reflex as rx
import adviento_web.styles.styles as styles 
from adviento_web.styles.styles import Color 
from adviento_web.components.header_text import header_text

def patners() -> rx.Component:
    return rx.center(
        rx.vstack(
            header_text(
                "star",
                "Patrocinadores",
                False
            ),
            rx.text(
                "Por el momento, este proyecto no cuenta con patrocinadores ya que estamos aprendiendo a programar con Python puro."
            ),
            rx.text(
                "Si quieres patrocinar este proyecto, puedes contactarme por gmail"
            ),
            max_width=styles.MAX_WIDTH,
            spacing="5"
        ),
        padding=styles.Size.DEFAULT.value,
        bg=Color.ACCENT.value,
        width="100%"
    )