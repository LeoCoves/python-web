import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.styles import styles




class State(rx.State):
    pass

#Definimos pantalla de inicio
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            links(),
            padding= styles.Size.VERY_BIG.value
        ),
        footer()
    )



#Añadimos index a la pagina
app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Link Bio",
    description="Link Bio es una aplicación web que te permite crear tu propia página de enlaces personalizada para compartir tus redes sociales, proyectos y mucho más."
)

