import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(f"© 2023-{datetime.datetime.today().year} by Leo Coves"),
        rx.text("Made with Reflex"),
        justify="center"
    )