import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.views.navbar import navbar
from adviento_web.views.header import header



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
                header(),
                spacing="9"
        )
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page( 
    index
)

app._compile()