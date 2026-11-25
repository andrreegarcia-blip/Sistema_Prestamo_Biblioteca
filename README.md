
# Sistema de Préstamo de Libros

## Descripción
Sistema desarrollado en Python para gestionar los préstamos y devoluciones de libros de la Biblioteca Comunal de Los Baños del Inca, Cajamarca.

El programa permite administrar los libros, registrar lectores y controlar los préstamos y devoluciones.

## Objetivo
Mejorar el control de los préstamos de libros mediante un sistema informático sencillo y organizado.

## Funcionalidades
- Registrar libros.
- Registrar lectores.
- Consultar libros disponibles.
- Registrar préstamos.
- Registrar devoluciones.
- Calcular multas por retraso.
- Guardar información en archivos JSON.
- Validar datos y controlar errores.

## Tecnologías utilizadas
- Python
- Visual Studio Code
- Archivos JSON
- Git y GitHub

## Estructura del proyecto
- modelo.py: administra los datos y las operaciones.
- vista.py: muestra el menú y los mensajes.
- controlador.py: controla las operaciones del sistema.
- main.py: inicia el programa.
- datos/: almacena la información.
- .gitignore: excluye archivos innecesarios.

## Ejecución
Para iniciar el sistema, ejecutar en la terminal:

```bash
python main.py
```

## Arquitectura
El proyecto utiliza el patrón MVC (Modelo-Vista-Controlador), separando la gestión de datos, la interfaz y el control de las operaciones.

## Almacenamiento
Los datos se guardan en formato JSON para conservar la información al cerrar el programa.
