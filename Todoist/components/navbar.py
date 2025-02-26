import reflex as rx
from ..styles.styles import Spacing, Colors


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.heading(
                    "Gestor de Tareas",
                    line_height="40px"
                ),
                href="/",
                text_decoration="none",
                color=Colors.NEGRO.value
            ),
            rx.link(
                "Acerca de",
                href="/about",
                text_align="center",
                line_height="30px",
                text_decoration="none",
                color=Colors.BLANCO.value,
                background_color=Colors.NEGRO.value,
                padding_y="5px",
                padding_x="10px",
                border_radius="5px",
                _hover={
                    "background_color": Colors.GRIS.value
                }
            ),
            justify="between",
            items="center",

        ),
        border_bottom="1px solid black",
        padding_bottom="10px",
    )
