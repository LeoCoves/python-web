import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.views.navbar import navbar
from adviento_web.views.header import header
from adviento_web.views.footer import footer
from adviento_web.views.instructions import instructions
from adviento_web.views.author import author
from adviento_web.views.patners import patners
from adviento_web.views.calendar import calendar



def index() -> rx.Component:
    return rx.box(
        rx.script(
            src="js/snow.js"
        ),
        navbar(),
        rx.vstack(
                header(),
                instructions(),
                calendar(),
                rx.separator(
                    margin_x="20%",
                    width="60%",
                ),
                author(),
                patners(),
                footer(),
                spacing="9",
                margin="0px",
                padding="0px"
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