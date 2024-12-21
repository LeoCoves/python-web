import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links


class State(rx.State):
    pass

#Definimos pantalla de inicio
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            links()
        ),
        footer()
    )



#Añadimos index a la pagina
app = rx.App()
app.add_page(index)



# import reflex as rx

# from rxconfig import config


# class State(rx.State):
#     """The app state."""

#     ...


# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to my Python Web Project!", size="9"),
#             rx.text(
#                 "Make it for Leo Coves",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#         rx.logo(),
#     )


# app = rx.App()
# app.add_page(index)
