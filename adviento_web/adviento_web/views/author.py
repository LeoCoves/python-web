import reflex as rx
from adviento_web.components.header_text import header_text
from adviento_web.components.button import button
from adviento_web.styles import styles

def author() -> rx.Component:
    return rx.center(
        rx.vstack(
            header_text(
                "like",
                "Hola, mi nombre es Leo Coves"
            ),
            rx.hstack(
                rx.flex(
                    rx.avatar(
                        name="Leo Coves",
                        radius="full",
                        size="8",
                        margin_right=styles.Size.DEFAULT.value,
                        margin_bottom=styles.Size.DEFAULT.value,
                        src="perfil.jpg",
                        alt="Perfil de Leo Coves",
                        align_self="center"
                    ),
                    rx.vstack(
                        rx.text.span(
                            "Soy estudiante de Desarrollo de Aplicaciones Web en Alicante"
                        ),
                        rx.text.span(
                            "Actualmente estoy aprendiendo Python y sus diferentes frameworks para desarrollar mis habilidades fuera del ambito escolar"
                        ),
                        author_buttons()
                    ),
                    flex_direction=["column", "column", "row"]
                )
            ),
            max_width=styles.MAX_WIDTH
        ),
        width="100%"
    )

def author_buttons() -> rx.Component:
    return rx.box(
        rx.flex(
            button(
                "Linkedin",
                "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
            ),
            button(
                "Github",
                "https://github.com/LeoCoves/python-web/tree/main/adviento_web"
            ),
            button(
                "Gmail",
                 "https://mail.google.com/mail/?view=cm&fs=1&to=l.covesguzman@gmail.com"
            ),
            button(
                "Curriculum",
                ""
            ),
            width="100%",
            justify_content="space-around",
        )
    )