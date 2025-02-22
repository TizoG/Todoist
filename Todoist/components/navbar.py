import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading(
                "Gestor de Tareas",
            ),
            rx.link(
                "Acerca de",
                href="#",
                text_align="center",
                line_height="30px",
            ),
            justify="between",
            items="center",

        )
    )
