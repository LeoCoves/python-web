import reflex as rx
import link_bio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title,
        margin=styles.Size.SMALL.value,
        margin_top=styles.Size.BIG.value
    )