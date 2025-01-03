import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.vstack(
                rx.text(
                    "© 2025 Adviento"
                ),
                rx.text(
                    "Creado con Reflex por Leo Coves"
                )
            ),
            rx.spacer(),
            rx.image(
                src="logo.png",
                alt="Logo de Leo Coves",
                width=Size.BIG.value,
                height=Size.BIG.value
            ),
            max_width=styles.MAX_WIDTH
        ),
        width="100%"
    )