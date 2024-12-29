import reflex as rx
from link_bio.components.link_button  import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title(
            "Mis redes Sociales"
        ),
        link_button(
            "linkedin",
            "LinkedIn", 
            "Averigua más sobre mi",
            "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
        ),
        link_button(
            "github",
            "Github", 
            "Mis proyectos",
            "https://github.com/LeoCoves"
        ),
        link_button(
            "twitter",
            "Twitter", 
            "Mis pensamientos",
            "https://twitter.com/LeoCoves"
        ),
        link_button(
            "instagram",
            "Instagram", 
            "Mas personal",
            "https://www.instagram.com/leocovess/"
        ),
        title(
            "Contactame"
        ),
        link_button(
            "user",
            "Mi CV", 
            "Mis experiencias",
            "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
        ),
        link_button(
            "messages-square",
            "Gmail", 
            "Enviame un correo",
            "hgnttps://github.com/LeoCoves"
        ),
        link_button(
            "phone-forwarded",
            "Wasap", 
            "Contactame mas rapido",
            "https://twitter.com/LeoCoves"
        )
    )