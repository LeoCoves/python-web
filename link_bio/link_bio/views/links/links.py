import reflex as rx
from link_bio.components.link_button  import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button(
            "at-sign",
            "LinkedIn", 
            "Averigua más sobre mi",
            "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
        ),
        link_button(
            "at-sign",
            "GitHub", 
            "Mis proyectos",
            "https://github.com/LeoCoves"
        ),
        link_button(
            "at-sign",
            "Twitter", 
            "Mis pensamientos",
            "https://twitter.com/LeoCoves"
        ),
        link_button(
            "at-sign",
            "Instagram", 
            "Mas personal",
            "https://www.instagram.com/leocovess/"
        )
    )