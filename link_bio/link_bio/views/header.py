import reflex as rx
from datetime import datetime
from link_bio.styles.styles import Size as Size
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import TextColor as TextColor
from link_bio.styles.styles import Color as Color

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
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
                        color=TextColor.HEADER.value
                    ),
                    rx.text(
                        "@leocovess",
                        margin_top="0px !important",
                        size="2",
                        color=Color.PRIMARY.value
                    ),
                    rx.hstack(
                        link_icon(
                            "linkedin", 
                            "https://www.linkedin.com/in/leo-coves-guzman-b68554281/",
                            "Logotipo de linkedin"
                        ),
                        link_icon(
                            "github", 
                            "https://github.com/LeoCoves",
                            "Logotipo de Github"
                        ),
                        link_icon(
                            "instagram", 
                            "https://www.instagram.com/leocovess/",
                            "Logotipo de Instagram"
                        ),
                        link_icon(
                            "messages-square", 
                            "https://mail.google.com/mail/?view=cm&fs=1&to=l.covesguzman@gmail.com",
                            "Logotipo de Gmail"
                        )
                    )
                )
            ),
            rx.text(
                "Mi nombre es Leo Coves, tengo 19 años y soy Desarrollador de Aplicaciones Web Junior. "
                "Me encanta aprender y compartir mis pequeños proyectos mientras amplio mi conocimiento conociendo mas tecnologias y profundizando en ellas. "
                "Ahora mismo estoy creando mi portafolio personal usando Python Puro y Reflex(Framework).",
                text_align="center"
            ),
            color=TextColor.BODY.value,
            spacing="8",
            max_width="1000px"
        ),
        width="100%"
    )