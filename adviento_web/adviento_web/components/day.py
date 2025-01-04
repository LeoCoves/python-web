import reflex as rx
from adviento_web.styles.styles import Color, Text_Color

def day(number: int, image: str = "gift.png", url: str = "") -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.link(
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al dia {number}"
                ),
                href=url,
                is_external=True,
                position="absolute"
            )
        ),
        rx.cond(
            url == "",
            rx.link(
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al dia {number}",
                    position="absolute"
                )       
            )
        ),
        rx.text(
            number,
            position="absolute"
        ),
        bg=Color.ACCENT.value,
        width="100%",
        aspect_ratio="1",
        position="relative"
    )