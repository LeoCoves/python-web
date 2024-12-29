import reflex as rx
from link_bio.components.link_button  import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("LinkedIn", "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"),
        link_button("GitHub", "https://github.com/LeoCoves"),
        link_button("Twitter", "https://twitter.com/LeoCoves"),
        link_button("Instagram", "https://www.instagram.com/leocovess/")
    )