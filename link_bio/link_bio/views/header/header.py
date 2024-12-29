import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="LC",
                radius="large",
                size="6"
            ),
            rx.vstack(
                rx.heading(
                    "Leo Coves",
                    size="5"
                ),
                rx.text(
                    "@leocovess",
                    margin_top="0px !important"
                )
            )
        ),
        rx.text(
            """Soy un desarrollador de software.
            Me encanta aprender y compartir conocimientos.
            Ahora mismo estoy creando mi portafolio personal."""
        )
    )