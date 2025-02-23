import reflex as rx
import datetime
from reflex import state


class GestorTareas:

    def __init__(self):
        # Creamos las variables para almacenar tareas y estados
        self.tareas = []  # lista para almacenar tareas
        self.estado = ["pendiente", "en progreso",
                       "completada"]  # lista de estados posibles
        self.id = 1  # identificador unico para cada tarea

# Creamos los metodos
# Metodo para agregar tareas
    def agregar_tarea(self, tarea, descripcion, estado):
        """"
        Agrega una nueva tarea con titulo, descripcion y estado.
        Args:
            tarea(str): titulo de la tarea
            descripcion(str): descripcion de la tarea
            estado(str): estado de la tarea
        """
        # Comprobamos que el estado sea correcto
        if estado not in self.estado:
            print("debes introducir un estado correcto.")
        else:
            # Creamos la tarea con la fecha actual y la agregamos a la lista
            fecha_actual = datetime.datetime.now()
            self.tareas.append(
                {
                    "ID": self.id,
                    "Titulo": tarea,
                    "Descripcion": descripcion,
                    "Fecha": fecha_actual.strftime("%d/%m/%Y %H:%M:%S"),
                    "Estado": estado

                })
            print("Tarea agregada.")
            self.id += 1  # incrementamos el id


gestor = GestorTareas()


class State(rx.State):
    titulo: str = ""
    descripcion: str = ""
    estado: str = ""

    def agregar(self):
        gestor.agregar_tarea(self.titulo, self.descripcion, self.estado)
        self.titulo = ""
        self.descripcion = ""
        self.estado = ""


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
                        on_change=State.set_titulo,
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
                        on_change=State.set_descripcion
                    ),
                ),
                rx.hstack(
                    rx.text(
                        "Introduce el estado (pendiente, en progreso, completada): ",
                        line_height="32px"
                    ),
                    rx.input(
                        placeholder="Estado de la tarea",
                        value=State.estado,
                        on_change=State.set_estado
                    ),
                ),
                rx.button(
                    "Agregar",
                    on_click=State.agregar
                ),
                rx.vstack(
                    *[rx.text(
                        f"{tarea["ID"]}: {tarea["Titulo"]} - {tarea["Descripcion"]} {tarea["Fecha"]} {tarea["Estado"]}"
                    ) for tarea in gestor.tareas]
                )
            )
        ),
        background_color="gray",
        margin_top="20px",
        border_radius="10px",
    )
