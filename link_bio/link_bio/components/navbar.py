import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Leo Coves", 
            color="blue", 
            height="40px", 
            size="5"
        ),
        position="sticky",
        text_align="center"
    )