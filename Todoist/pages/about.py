import reflex as rx
from ..components.navbar import navbar
from ..components.texto_about import text_about


def about() -> rx.Component:
    return rx.container(
        navbar(),
        rx.vstack(
            text_about()
        )
    )
