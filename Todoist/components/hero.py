import reflex as rx
from reflex import state
from ..state import State
from ..styles.styles import Spacing, Colors


def toltips():
    State.agregar_tarea(),

    rx.toast.success(
        "Tarea agregada correctamente",
        duration=5000,
        close_button=True
    ),


def hero() -> rx.Component:

    return rx.container(
        rx.box(
            rx.vstack(
                rx.text(
                    "Agregar tarea",
                    font_size="24px",
                    text_align="center"
                ),
                rx.hstack(
                    rx.text(
                        "Introduce el titulo: ",
                        line_height="32px",
                    ),
                    rx.input(
                        placeholder="Titulo de la tarea",
                        value=State.titulo,
                        on_change=State.set_titulo

                    ),
                ),
                rx.hstack(
                    rx.text(
                        "Introduce la descripción: ",
                        line_height="32px"
                    ),
                    rx.input(
                        placeholder="Descripción de la tarea",
                        value=State.descripcion,
                        on_change=State.set_descripcion,
                    ),
                ),
                rx.hstack(
                    rx.text(
                        "Intoduce el estado"
                    ),
                    rx.select(
                        ["Pendiente", "En progreso", "Completada"],
                        default_value="pendiente",
                        required=True,
                        value=State.estado,
                        on_change=State.set_estado
                    )
                ),
                rx.tooltip(
                    rx.button(
                        "Agregar",
                        on_click=[
                            State.agregar_tarea,
                            lambda: rx.toast.success(
                                "Tarea agregada correctamente",
                                duration=5000,
                                close_button=True
                            )
                        ],
                    ),
                    content="Agrega una nueva tarea"
                ),


            )
        ),
        background_color=Colors.GRIS.value,
        margin_top="20px",
        border_radius="10px",
    )
