import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.components.button import button as button

def instructions() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.text(
                    "¿Como jugar?",
                    class_name="title",
                    color=styles.Color.ACCENT.value
                ),
                rx.text.span(
                    "· Del 1 al 24 de diciembre, se publicará un reto diario en el que tendrás que resolver un problema de programación."
                ),
                rx.text.span(
                    "· Puedes resolver el reto en el lenguaje de programación que prefieras."
                ),
                rx.text.span(
                    "· Para enviar tu solución, deberás hacer un pull request en el repositorio de GitHub."
                ),
                button(
                    "GitHub",
                    "https://github.com/LeoCoves/python-web"
                ),
                rx.text.span(
                    "· Si tienes alguna duda, puedes contactarme por cualquiera de mis redes sociales."
                ),
                button(
                    "Instagram",
                    "https://www.instagram.com/leocovess/"
                ),
                rx.text.span(),
                class_name="nes-container is-dark with-title",
                width="100%",
                padding=styles.Size.DEFAULT.value
            ),
            max_width = styles.MAX_WIDTH
        ),
        width="100%"
    )