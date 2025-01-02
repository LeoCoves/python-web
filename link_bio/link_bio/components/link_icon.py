import reflex as rx
import link_bio.styles.styles as styles

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            icon
        ),
        href=url, 
        is_external=True,
        size="2"
    )