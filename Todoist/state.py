import reflex as rx
import datetime


class State(rx.State):
    """
    Clase que maneja el estado global de la aplicacion.
    """
    titulo: str = ""
    descripcion: str = ""
    estado: str = "Pendiente"
    tareas: list[dict] = []

    @rx.event
    def agregar_tarea(self):
        """"
        Agrega una nueva tarea
        """
        fecha_actual = datetime.datetime.now()
        nueva_tarea = {
            "ID": len(self.tareas) + 1,
            "Titulo": self.titulo,
            "Descripcion": self.descripcion,
            "Fecha": fecha_actual.strftime("%d/%m/%Y %H:%M:%S"),
            "Estado": self.estado
        }
        self.tareas.append(nueva_tarea)

        # Reiniciamos valores
        self.titulo = ""
        self.descripcion = ""
        self.estado = "Pendiente"

    @rx.event
    def eliminar_tarea(self, tarea_id):
        self.tareas = [
            tarea for tarea in self.tareas if tarea["ID"] != tarea_id]

    @rx.event
    def modificar_tarea(self, tarea_id):
        for tarea in self.tareas:
            if tarea["ID"] == tarea_id:
                tarea["Estado"] = self.estado
