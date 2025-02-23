
import reflex as rx
from reflex import theme
from rxconfig import config
from .components.navbar import navbar
from .components.hero import hero


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        hero(),
    )


app = rx.App(
    theme=theme(
        color_mode="light",
    ),
    style={"background_color": "#F7F7F7"}
)
app.add_page(index)
