import reflex as rx
from link_bio.components.link_button  import link_button
from link_bio.components.title import title
from link_bio.constants import URL

def links() -> rx.Component:
    return rx.center(
        rx.vstack(
            title(
                "Mis redes Sociales"
            ),
            link_button(
                "linkedin",
                "LinkedIn", 
                "Averigua más sobre mi",
                URL.URL_LINKEDIN,
                "Logotipo de LinkedIn",
                False
            ),
            link_button(
                "github",
                "Github", 
                "Mis proyectos",
                URL.URL_GITHUB,
                "Logotipo de Github",
                False
            ),
            link_button(
                "twitter",
                "Twitter", 
                "Mis pensamientos",
                URL.URL_TWITTER,
                "Logotipo de Twitter",
                True
            ),
            link_button(
                "instagram",
                "Instagram", 
                "Mas personal",
                URL.URL_INSTAGRAM,
                "Logotipo de Instagram",
                False
            ),
            title(
                "Contactame"
            ),
            link_button(
                "user",
                "Mi CV", 
                "Mis experiencias",
                URL.URL_CV,
                "Logotipo de un CV",
                False
            ),
            link_button(
                "messages-square",
                "Gmail", 
                "Enviame un correo",
                URL.URL_GMAIL,
                "Logotipo de Gmail",
                False
            ),
            link_button(
                "phone-forwarded",
                "WhatsApp", 
                "Contactame mas rapido",
                URL.URL_WHATSAPP,
                "Logotipo de Whatsapp",
                True
            )
        ),
        width="100%",
        padding_x="15%"
    )