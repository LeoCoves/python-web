import reflex as rx
from link_bio.components.link_button  import link_button
from link_bio.components.title import title

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
                "https://www.linkedin.com/in/leo-coves-guzman-b68554281/",
                "Logotipo de LinkedIn"
            ),
            link_button(
                "github",
                "Github", 
                "Mis proyectos",
                "https://github.com/LeoCoves",
                "Logotipo de Github"
            ),
            link_button(
                "twitter",
                "Twitter", 
                "Mis pensamientos",
                "https://twitter.com/LeoCoves",
                "Logotipo de Twitter"
            ),
            link_button(
                "instagram",
                "Instagram", 
                "Mas personal",
                "https://www.instagram.com/leocovess/",
                "Logotipo de Instagram"
            ),
            title(
                "Contactame"
            ),
            link_button(
                "user",
                "Mi CV", 
                "Mis experiencias",
                "https://www.linkedin.com/in/leo-coves-guzman-b68554281/",
                "Logotipo de un CV"
            ),
            link_button(
                "messages-square",
                "Gmail", 
                "Enviame un correo",
                "https://mail.google.com/mail/?view=cm&fs=1&to=l.covesguzman@gmail.com",
                "Logotipo de Gmail"
            ),
            link_button(
                "phone-forwarded",
                "Wasap", 
                "Contactame mas rapido",
                "https://web.whatsapp.com/send?phone=34675181093",
                "Logotipo de Whatsapp"
            )
        ),
        width="100%",
        padding_x="15%"
    )