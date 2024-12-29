import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.styles import styles




class State(rx.State):
    pass

#Definimos pantalla de inicio
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links()
            )
        ),
        footer()
    )



#Añadimos index a la pagina
app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)

