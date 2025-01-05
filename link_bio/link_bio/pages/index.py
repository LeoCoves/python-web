import reflex as rx
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links
from link_bio.styles import styles
from link_bio.routes import Route

rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    meta=utils.index_meta
)

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


