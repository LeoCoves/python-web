import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import TextColor as TextColor
from link_bio.styles.styles import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="perfil.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                radius="full",
                size="7"
            ),
            rx.vstack(
                rx.heading(
                    "Leo Coves",
                    size="4",
                    color=TextColor.HEADER
                ),
                rx.text(
                    "@leocovess",
                    margin_top="0px !important",
                    size="2",
                    color=TextColor.BODY
                ),
                rx.hstack(
                    link_icon(
                        "linkedin", 
                        "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                    ),
                    link_icon(
                        "github", 
                        "https://github.com/LeoCoves"
                    ),
                    link_icon(
                        "instagram", 
                        "https://www.instagram.com/leocovess/"
                    ),
                    link_icon(
                        "messages-square", 
                        "https://mail.google.com/mail/?view=cm&fs=1&to=l.covesguzman@gmail.com"
                    )
                )
            )
        ),
        rx.text(
            """Soy un desarrollador de software.
            Me encanta aprender y compartir conocimientos.
            Ahora mismo estoy creando mi portafolio personal.""",
            text_align="center"
        ),
        color=TextColor.BODY.value,
        spacing="8",
        margin_bottom="5%"
    )