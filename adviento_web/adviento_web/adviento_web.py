import reflex as rx
from adviento_web.styles import styles as styles


def index() -> rx.Component:
    return rx.box(
        rx.text("¡Bienvenido a Adviento!"),
        rx.text("En esta página encontrarás una serie de problemas matemáticos que se irán liberando cada día del mes de diciembre."),
        rx.text("Cada problema tiene una solución que se puede enviar a través de un formulario.")
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page( 
    index
)

app._compile()