import reflex as rx
from adviento_web.styles.styles import Size as Size
from adviento_web.styles.colors import Color as Color
from adviento_web.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.center(
                rx.image(
                    src="santa.png",
                    alt="Imagen pixelada de Santa Claus",
                    width=Size.BIG.value,
                    height=Size.BIG.value
                ),
                rx.text(
                    "aDEViento 2024",
                    padding=Size.SMALL.value
                )
            ),
            rx.spacer(),
            rx.hstack(
                link_icon(
                    "linkedin",
                    "https://www.linkedin.com/in/leo-coves-guzman-b68554281/"
                ),
                link_icon(
                    "github",
                    "https://github.com/LeoCoves/python_web/adviento_web"
                ),
                link_icon(
                    "instagram",
                    "https://www.instagram.com/leocovess/"
                ),
                spacing="6"
            ),
            width="100%"
        ),
        width="100%",
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=1000,
        top=0,
    )