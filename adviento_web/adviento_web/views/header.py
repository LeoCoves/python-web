import reflex as rx
from adviento_web.styles.styles import Size, Text_Color
from adviento_web.styles import styles as styles

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Calendario de Adviento",
                size="7",
                padding_bottom=Size.DEFAULT.value,
                padding=Size.MEDIUM.value
            ),
            rx.flex(
                rx.image(
                    src="santa.png",
                    alt="Imagen pixelada de Santa Claus",
                    width="16em",
                    height="16em",
                    margin_right=Size.BIG.value,
                    align_self="center"
                ),
                rx.vstack(
                    rx.tablet_and_desktop(
                        rx.box(
                            rx.text(
                                "24 dias. 24 regalos"
                            ),
                            rx.text(
                                "Del 1 al 24 de diciembre"
                            ),
                            class_name="nes-balloon from-left is-dark"
                        )
                    ),
                    rx.mobile_only(
                        rx.box(
                            rx.text(
                                "24 dias. 24 regalos"
                            ),
                            rx.text(
                                "Del 1 al 24 de diciembre"
                            ),
                            class_name="nes-balloon from-right is-dark"
                        )
                    ),
                    rx.text.span(
                        "Por segundo año, ¡aquí está el calendario de adviento sorpresa de nuestra",
                        rx.text.span(
                            " comunidad de desarrolladores web",
                            color=Text_Color.ACCENT.value,
                            font_size=Size.DEFAULT.value
                        ),
                        "!"
                    ),  
                    rx.text.span(
                        "Una actividad para compartir conocimientos, aprender y disfrutar de la navidad."
                    ),
                    rx.text.span(
                        "Su finalidad es fomentar la creatividad y la colaboración entre los"
                    ),
                    rx.link(
                        "#aDEViento",
                        href="https://linkedin.com/in/leo-coves-guzman-b68554281",
                        is_external=True,
                        color= Text_Color.TERTIARY.value,
                        padding_top=Size.BIG.value,
                        font_size=Size.DEFAULT.value,
                        width="100%",
                        text_align="start"
                    )
                ),
                flex_direction=["column", "column", "column", "row"],
            ),
            max_width=styles.MAX_WIDTH
        ),
        width="100%"
    )