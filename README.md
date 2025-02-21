# Gestor de Tareas con Reflex

Una aplicación web para gestionar tareas (al estilo Todoist) utilizando el framework Reflex en Python. La aplicación permite crear, modificar, eliminar y visualizar tareas, y persiste la información en un archivo JSON para mantener los datos entre sesiones.

## Características

-   **Agregar Tarea:**  
    Permite crear tareas con título, descripción, estado y fecha de creación.
-   **Modificar Tarea:**  
    Edita la descripción y el estado de las tareas existentes.

-   **Eliminar Tarea:**  
    Elimina una tarea seleccionada de la lista.

-   **Persistencia de Datos:**  
    Todas las tareas se guardan en un archivo JSON (`tareas.json`) para mantener la información entre sesiones.

-   **Interfaz Reactiva:**  
    La aplicación se actualiza de forma dinámica al realizar cambios, sin necesidad de recargar la página.

## Arquitectura y Diseño de la Aplicación

### Barra de Navegación (Menú Superior)

-   Ubicada en la parte superior.
-   Contiene el título de la aplicación ("Gestor de Tareas") y, opcionalmente, enlaces a secciones adicionales (como Acerca de o Ajustes).

### Área Principal

#### Sección de Agregar Tarea

-   Formulario con campos para **título**, **descripción** y **estado** (seleccionable entre "pendiente", "en progreso" y "completada").
-   Botón para agregar la tarea.
-   Ubicado inmediatamente debajo de la barra de navegación en un contenedor centrado.

#### Sección de Visualización de Tareas

-   Las tareas se muestran en tarjetas o cajas.
-   Cada tarjeta contiene:
    -   **Título**, **Descripción**, **Fecha de creación** y **Estado**.
    -   Botones para **modificar** y **eliminar** la tarea, además de opciones para cambiar el estado.
-   Las tarjetas se disponen en un layout responsivo (por ejemplo, en grid en pantallas grandes y en lista vertical en dispositivos móviles).

### Gestión del Estado y Persistencia

-   **Clase de Estado (`Estado`):**  
    Centraliza la lógica de negocio (agregar, modificar, eliminar tareas) y persiste los datos en un archivo JSON.
-   **Persistencia:**  
    Métodos para guardar (`guardar_tareas`) y cargar (`cargar_tareas`) la información de las tareas desde/hacia `tareas.json`.

## Guía de Estilos y Diseño Visual

### Paleta de Colores

-   **Fondo de la Aplicación:**
    -   Blanco (#FFFFFF) o gris muy claro (#F7F7F7) para transmitir limpieza y modernidad.
-   **Tarjetas de Tarea (según estado):**
    -   _Pendiente:_ Gris suave (#E0E0E0)
    -   _En progreso:_ Azul pastel (#AEDFF7)
    -   _Completada:_ Verde suave (#B8E986)
-   **Botones y Acentos:**
    -   Botón "Agregar": Azul vibrante (#007BFF)
    -   Botón "Eliminar": Rojo (#FF4C4C)
    -   Botones secundarios (modificar, etc.): Tonos neutros o gris oscuro.

### Fuentes y Tamaños

-   **Fuente Principal:**  
    Se recomienda usar **Roboto**, **Open Sans** o **Lato**.
-   **Tamaños Sugeridos:**
    -   Títulos de tareas: 20–24px.
    -   Descripciones y textos secundarios: 14–16px.
    -   Botones: 14px con un buen padding (por ejemplo, 8px 16px).

### Espaciado y Layout

-   **Margen y Padding:**  
    Entre 10 y 20px para separar los elementos.
-   **Diseño de Tarjetas:**
    -   Bordes redondeados (5–10px).
    -   Sombra sutil para profundidad (`box-shadow: 0 2px 4px rgba(0,0,0,0.1)`).
-   **Disposición Responsiva:**  
    La interfaz se adapta a distintos tamaños de pantalla, organizando las tarjetas en columnas en desktop y en una sola columna en dispositivos móviles.

## Instalación y Ejecución

1. **Clonar el repositorio:**
    ```bash
    git clone https://tu-repositorio.git
    cd mi_app_tareas
    ```

## Contribución

Si deseas colaborar o mejorar este proyecto, ¡tus aportaciones son bienvenidas! Puedes abrir issues o enviar pull requests.

## Licencia

Este proyecto se distribuye bajo la licencia .
