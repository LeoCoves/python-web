import reflex as rx
import datetime
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles import styles as styles
from link_bio.constants import URL

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.center(
                rx.image(
                    src="logo.png",
                    width=styles.Size.VERY_BIG.value,
                    height=styles.Size.VERY_BIG.value,
                    alt="Logotipo de la página"
                ),
                width="100%"
            ),
            rx.link(
                rx.text(
                    f"© 2023-{datetime.datetime.today().year} by Leo Coves"
                ),
                color=TextColor.FOOTER,
                href=URL.URL_CV,
                is_external=True
            ),
            rx.link(
                rx.text(
                    "Made with Reflex",
                    font_size=styles.Size.DEFAULT.value,
                    color=TextColor.FOOTER,
                    text_align="center"
                ),
                href=URL.URL_REFLEX,
                is_external=True
            ),
            margin_bottom=styles.Size.BIG.value,
            width="100%",
            text_align="center"
        )
    )