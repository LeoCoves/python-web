import reflex as rx
import datetime
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles import styles as styles

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="logo.png",
                width=styles.Size.VERY_BIG.value,
                margin_x= "47%"
            ),
            rx.link(
                rx.text(
                    f"© 2023-{datetime.datetime.today().year} by Leo Coves"
                ),
                color=TextColor.FOOTER,
                width="100%"
            ),
            rx.link(
                rx.text(
                    "Made with Reflex",
                    margin_top=styles.Size.SMALL.value,
                    font_size=styles.Size.MEDIUM.value,
                    text_align="center"
                )
            ),
            margin_bottom=styles.Size.BIG.value,
            padding_bottom=styles.Size.BIG.value,
            width="100%",
            text_align="center"
        )
    )