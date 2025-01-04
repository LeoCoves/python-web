import reflex as rx
from adviento_web.styles import styles
from adviento_web.components.header_text import header_text
from adviento_web.components.day import day

def calendar() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                header_text(
                    "heart",
                    "Calendario del aDEViento",
                    False
                ),
                rx.hstack(
                    rx.text(
                        "El evento comienza en "
                    ),
                    rx.text(
                        id="countdown"
                    )
                ),
                rx.text.span(
                    "·Los regalos son sorpresa, permaneceran ocultos hasta el dia de su apertura"
                )
            ),
            rx.grid(
                rx.foreach(
                    list(range(1, 25)), 
                    lambda number: 
                        day(
                            number
                        )
                ),
                columns="repeat(auto-fill, minmax(150px, 1fr))",
                rows="repeat(auto-fill, minmax(150px, 1fr))",
                gap=styles.Size.SMALL.value,
                width="100%",
                padding_top=styles.Size.DEFAULT.value
            ),
            rx.script(
                src="js/countdown.js"
            ),
            max_width=styles.MAX_WIDTH,
        ),
        width="100%",
    )