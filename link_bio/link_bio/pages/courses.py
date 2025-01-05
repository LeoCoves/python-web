import reflex as rx
import link_bio.utils as utils
from link_bio.styles import styles
from link_bio.routes import Route
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links


rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    meta=utils.courses_meta
)

#Definimos pantalla de inicio
def courses() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            links(),
            padding= styles.Size.VERY_BIG.value
        ),
        footer()
    )