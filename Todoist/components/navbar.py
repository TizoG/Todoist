import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading(
                "Gestor de Tareas",
                line_height="40px"
            ),
            rx.link(
                "Acerca de",
                href="#",
                text_align="center",
                line_height="30px",
                text_decoration="none",
                color="white",
                background_color="black",
                padding_y="5px",
                padding_x="10px",
                border_radius="5px",
                _hover={
                    "background_color": "gray"
                }
            ),
            justify="between",
            items="center",

        ),
        border_bottom="1px solid black",
        padding_bottom="10px",
    )
