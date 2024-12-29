import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="LC",
                radius="full",
                size="6"
            ),
            rx.vstack(
                rx.heading(
                    "Leo Coves",
                    size="5"
                ),
                rx.text(
                    "@leocovess",
                    margin_top="0px !important",
                    size="2"
                ),
                rx.hstack(
                    link_icon(
                        "at-sign", 
                        "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                    ),
                    link_icon(
                        "at-sign", 
                        "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                    ),
                    link_icon(
                        "at-sign", 
                        "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                    ),
                    link_icon(
                        "at-sign", 
                        "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                    )
                )
            )
        ),
        rx.text(
            """Soy un desarrollador de software.
            Me encanta aprender y compartir conocimientos.
            Ahora mismo estoy creando mi portafolio personal."""
        ),
        spacing="4"
    )