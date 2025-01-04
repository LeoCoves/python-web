import reflex as rx
import datetime
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles import styles as styles

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
                href="/download/CVdev.pdf",
                is_external=True
            ),
            rx.link(
                rx.text(
                    "Made with Reflex",
                    font_size=styles.Size.DEFAULT.value,
                    color=TextColor.FOOTER,
                    text_align="center"
                ),
                href="https://reflex.dev/docs/library/",
                is_external=True
            ),
            margin_bottom=styles.Size.BIG.value,
            width="100%",
            text_align="center"
        )
    )