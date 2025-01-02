import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.views.navbar import navbar



def index() -> rx.Component:
    return rx.box(
        navbar(),
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