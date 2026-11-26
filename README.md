# Sistema de Préstamo de Libros

## Descripción
Sistema informático desarrollado en Python para gestionar los préstamos y devoluciones de libros de la Biblioteca Comunal de Los Baños del Inca, Cajamarca.

El proyecto cuenta con una aplicación web desarrollada con Flask que permite administrar libros, lectores, préstamos y devoluciones de manera sencilla y organizada.

## Objetivo
Mejorar el control de los préstamos de libros mediante un sistema informático que facilite la administración de la biblioteca.

## Funcionalidades
- Registrar libros.
- Consultar libros disponibles.
- Eliminar libros.
- Registrar lectores.
- Registrar préstamos.
- Registrar devoluciones.
- Controlar la disponibilidad de los libros.
- Calcular multas por retraso.
- Guardar información en archivos JSON.
- Validar las operaciones del sistema.

## Tecnologías utilizadas
- Python.
- Flask.
- HTML.
- CSS.
- Archivos JSON.
- Visual Studio Code.
- Git y GitHub.

## Estructura del proyecto
- `app.py`: inicia la aplicación web y administra las rutas.
- `modelo.py`: administra los datos y las operaciones.
- `vista.py`: contiene la interfaz de consola original.
- `controlador.py`: controla las operaciones del sistema.
- `main.py`: inicia la versión de consola.
- `templates/`: contiene las páginas HTML.
- `static/`: almacena los archivos CSS.
- `datos/`: almacena la información en archivos JSON.

## Instalación y ejecución

1. Instalar Python.
2. Instalar Flask ejecutando en la terminal:

```bash
pip install flask
```

3. Abrir la carpeta del proyecto en Visual Studio Code.
4. Ejecutar el siguiente comando:

```bash
python app.py
```

5. Abrir el navegador e ingresar a:

```text
http://127.0.0.1:5000
```

## Arquitectura
El proyecto utiliza el patrón MVC (Modelo-Vista-Controlador), separando la gestión de datos, el control de las operaciones y la interfaz del sistema.

La aplicación web utiliza Flask para conectar las páginas HTML con las funciones desarrolladas en Python.

## Almacenamiento
La información se almacena en archivos JSON, permitiendo conservar los datos de libros, lectores y préstamos.

## Control de versiones
El proyecto utiliza Git y GitHub para registrar los avances y mantener el código fuente organizado.