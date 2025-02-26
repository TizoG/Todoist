import reflex as rx


def text_about() -> rx.Component:
    return rx.box(
        rx.heading(
            "Acerca de esta Sección:",
            margin_y="15px",

        ),

        rx.text(
            "Esta sección de la web permite a los usuarios gestionar sus tareas de manera eficiente, proporcionando funcionalidades para agregar, modificar y eliminar tareas. A continuación, se explican las siguientes funcionalidades:",
            margin_bottom="20px"
        ),
        rx.text(
            "Agregar Tareas",
            size="5",
            margin_bottom="10px"
        ),
        rx.text(
            "- El usuario puede crear una tarea introduciendo un título, descripción y un estado."
        ),
        rx.text(
            "- Cuando el usuario presione el botón Agregar, la tarea se guarda en la lista interna y se muestra en la interfaz con los valores introducidos."
        ),
        rx.text(
            "- El estado inicial de la tarea es Pendiente, pero puede ser modificada más adelante."
        ),
        rx.text(
            "Modificar Tarea",
            margin_top="25px",
            margin_bottom="10px",
            size="5"
        ),
        rx.text(
            "- Cada tarea tiene un botón de modificar, representado por un icono de un lápiz."
        ),
        rx.text(
            "- Al presionar este botón, el estado de edición de la tarea se activa, lo que permite al usuario cambiar el estado de la tarea."
        ),
        rx.text(
            "- Se ofrece un selector (dropdown) que permite elegir entre los tres estados disponibles: Pediente, En progreso y Completada. Este selector es el selector que tendremos en la seccion de agregar tarea, selecionaremos el estado que queremos que tenga nuestra tarea y le daremos a este boton en la tarea correspondiente."
        ),
        rx.text(
            "- El estado seleccionado se actualiza automáticamente en la lista de tareas y la interfaz refleja el cambio."
        ),
        rx.text(
            "Eliminar Tarea",
            margin_top="25px",
            margin_bottom="10px",
            size="5"
        ),
        rx.text(
            "Cada tarea también tiene un botón de eliminar, representado por un icono de papelera."
        ),
        rx.text(
            "Al hacer clic en este botón, la tarea se elimina de la lista de tareas, y se actualiza la interfaz para reflejar las tareas que tenmos activas."
        ),
        rx.text(
            "Interfaz dinamica",
            margin_top="25px",
            margin_bottom="10px",
            size="5"
        ),
        rx.text(
            "Las tareas se muestran de manera clara con su titulo, descripcion, fecha de creación y estado."
        ),
        rx.text(
            "Los colores de fondo de las tareas cambian según su estado:"
        ),
        rx.box(

            rx.text(
                "- Pendiente: gris",
                background_color="#E0E0E0"
            ),
            rx.text(
                "- En progreso: azul clato",
                background_color="#AEDFF7",
                margin_y="5px"  # Buscar la propiedad css para separar los elementos entre ellos, creando la propiedad en el contenedor
            ),
            rx.text(
                "- Completada: Verde claro",
                background_color="#B8E986",

            ),
            display="inline-block",
            margin_y="5px"


        ),
        rx.text(
            "Esto se logra mediante una condición que evalúa el estado de la tarea y asigna un color de fondo apropiado."
        )
    )
