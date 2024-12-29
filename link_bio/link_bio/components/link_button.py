import reflex as rx
import link_bio.styles.styles as styles

def link_button(icon: str, title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style = styles.button_title
                    ),
                    rx.text(
                        body,
                        style = styles.button_body
                    )
                )
            )
        ),
        href=url, 
        is_external=True
    )
        