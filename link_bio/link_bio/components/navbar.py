import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
            "Leo Coves", 
            color="blue"
            )
        ),
        position="sticky",
        padding=  "10px",
        z_index=999,
        bg="gray"
    )