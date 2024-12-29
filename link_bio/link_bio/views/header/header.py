import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="LC",radius="large"),
        rx.text("@leocovess"),
        rx.text("Hola, mi nombre es Leo Coves"),
        rx.text("Soy un desarrollador de software")
    )