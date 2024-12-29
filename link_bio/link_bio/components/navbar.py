import reflex as rx
from link_bio.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
            "leocoves", 
            color="blue",
            font_family="monospace"
            )
        ),
        position="sticky",
        padding=  "10px",
        z_index=999,
        bg=Color.CONTENT.value
    )