import reflex as rx
import datetime
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(
                src="logo.png",
                witdh="30px"
            ),
            rx.text(
                f"© 2023-{datetime.datetime.today().year} by Leo Coves"
            ),
            rx.text(
                "-Made with Reflex"
            ),
            color=TextColor.FOOTER
        )
    )