import reflex as rx
import link_bio.styles.styles as styles

def link_icon(icon: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.icon(
            icon,
            color=styles.TextColor.HEADER.value
        ),
        alt=alt,
        href=url, 
        is_external=True,
        size="2"
    )