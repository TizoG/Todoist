import reflex as rx
from ..state import State
from ..styles.styles import Spacing, Colors


def lista_tareas() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.tareas,
            lambda tarea: rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            f"ID: {tarea['ID']} - {tarea['Titulo']}", ),
                        rx.text(tarea['Descripcion']),
                        rx.text(f"Fecha creacion: {tarea['Fecha']}"),
                        rx.text(f"Estado: {tarea['Estado']}"),
                    ),
                    rx.hstack(
                        rx.tooltip(
                            rx.button(
                                rx.icon(
                                    "pen"
                                ),
                                on_click=[
                                    lambda: State.modificar_tarea(
                                        tarea["ID"]),
                                    rx.toast(
                                        "Tarea modificada correctamente",
                                        duration=5000,
                                        close_button=True
                                    )
                                ],
                                background_color=Colors.BLUE_ICON.value,
                                _hover={
                                    "cursor": "pointer",
                                    "background_color": Colors.BLUE_ICON_HOVER.value
                                }
                            ),
                            content="Modifica el estado de la tarea"
                        ),
                        rx.tooltip(
                            rx.button(
                                rx.icon(
                                    "trash-2"
                                ),
                                on_click=[
                                    lambda: State.eliminar_tarea(
                                        tarea["ID"]),
                                    rx.toast.error(
                                        "Tarea eliminada correctamente",
                                        duration=5000,
                                        close_button=True
                                    ),
                                ],
                                background_color="red",
                                _hover={
                                    "cursor": "pointer",
                                    "background_color": "tomato"}
                            ),
                            content="Elimina la tarea"
                        ),


                    ),
                    justify="between"
                ),
                background_color=rx.cond(
                    tarea["Estado"] == "Completada",
                    Colors.LIGHT_GREEN.value,
                    rx.cond(
                        tarea["Estado"] == "En progreso",
                        Colors.LIGTH_BLUE.value,
                        Colors.LIGTH_GRAY.value

                    )
                ),
                padding="15px",
                margin_y="15px",
                border_radius="20px"

            )
        )
    )
