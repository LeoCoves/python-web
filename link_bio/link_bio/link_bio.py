import reflex as rx
from link_bio.styles import styles
from link_bio.routes import Route
from link_bio.pages.index import index
from link_bio.pages.courses import courses




#Añadimos index a la pagina
app = rx.App(
    style=styles.BASE_STYLE
)

app.add_page(index, route=Route.INDEX.value)
app.add_page(courses, route=Route.COURSES.value)



