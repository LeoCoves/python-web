import reflex as rx
import link_bio.styles.styles as styles

def link_button(icon: str, title: str, body: str, url: str, alt: str, disabled: bool) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin = styles.Size.SMALL.value
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style = styles.button_title
                    ),
                    rx.text(
                        body,
                        style = styles.button_body
                    ),
                    text_align="start"
                )
            ),
            disabled=disabled
        ),
        alt=alt,
        href=url, 
        is_external=True
    )
        