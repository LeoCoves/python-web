import reflex as rx
from link_bio.components.link_button  import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title(
            "Mis redes Sociales"
        ),
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
        ),
        title(
            "Contactame"
        ),
        link_button(
            "at-sign",
            "Mi CV", 
            "Mis experiencias",
            "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
        ),
        link_button(
            "at-sign",
            "Gmail", 
            "Enviame un correo",
            "https://github.com/LeoCoves"
        ),
        link_button(
            "at-sign",
            "Wasap", 
            "Contactame mas rapido",
            "https://twitter.com/LeoCoves"
        )
    )