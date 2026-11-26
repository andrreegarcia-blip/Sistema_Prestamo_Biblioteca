
import json
import os
from datetime import date, timedelta

# Archivo JSON donde se almacena la información de la biblioteca.
ARCHIVO = "datos/datos_biblioteca.json"

libros = []
lectores = []
prestamos = []

MAX_PRESTAMOS = 3
PLAZO_DIAS = 7
MULTA_POR_DIA = 0.50


def guardar_datos() -> None:
    """Guarda la información de la biblioteca en un archivo JSON."""
    datos = {
        "libros": libros,
        "lectores": lectores,
        "prestamos": prestamos
    }

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_datos() -> None:
    """Carga los datos guardados anteriormente."""
    global libros, lectores, prestamos

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        libros = datos.get("libros", [])
        lectores = datos.get("lectores", [])
        prestamos = datos.get("prestamos", [])


def registrar_libro(codigo: str, titulo: str, autor: str) -> str:
    """Registra un nuevo libro en la biblioteca."""
    if any(libro["codigo"] == codigo for libro in libros):
        return "El código del libro ya existe."

    libros.append({
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    })

    guardar_datos()
    return "Libro registrado correctamente."


def registrar_lector(codigo: str, nombre: str) -> str:
    """Registra un nuevo lector."""
    if any(lector["codigo"] == codigo for lector in lectores):
        return "El código del lector ya existe."

    lectores.append({
        "codigo": codigo,
        "nombre": nombre
    })

    guardar_datos()
    return "Lector registrado correctamente."


def obtener_libros() -> list:
    """Devuelve la lista de libros registrados."""
    return libros


def obtener_lectores() -> list:
    """Devuelve la lista de lectores registrados."""
    return lectores


def obtener_prestamos() -> list:
    """Devuelve la lista de préstamos registrados."""
    return prestamos


def registrar_prestamo(codigo_libro: str, codigo_lector: str) -> str:
    """Registra un préstamo si cumple las condiciones."""

    libro = next(
        (l for l in libros if l["codigo"] == codigo_libro), None
    )

    lector = next(
        (l for l in lectores if l["codigo"] == codigo_lector), None
    )

    if libro is None:
        return "El libro no existe."

    if lector is None:
        return "El lector no existe."

    if not libro["disponible"]:
        return "El libro no está disponible."

    activos = sum(
        1 for p in prestamos
        if p["codigo_lector"] == codigo_lector
        and p["estado"] == "Activo"
    )

    if activos >= MAX_PRESTAMOS:
        return "El lector alcanzó el máximo de 3 préstamos."

    fecha_prestamo = date.today()
    fecha_devolucion = fecha_prestamo + timedelta(days=PLAZO_DIAS)

    prestamos.append({
        "codigo_libro": codigo_libro,
        "codigo_lector": codigo_lector,
        "fecha_prestamo": fecha_prestamo.isoformat(),
        "fecha_devolucion": fecha_devolucion.isoformat(),
        "estado": "Activo",
        "multa": 0.0
    })

    libro["disponible"] = False
    guardar_datos()

    return "Préstamo registrado correctamente."


def registrar_devolucion(codigo_libro: str) -> str:
    """Registra la devolución y calcula la multa correspondiente."""

    prestamo = next(
        (p for p in prestamos
         if p["codigo_libro"] == codigo_libro
         and p["estado"] == "Activo"),
        None
    )

    if prestamo is None:
        return "No existe un préstamo activo para este libro."

    fecha_limite = date.fromisoformat(prestamo["fecha_devolucion"])
    fecha_actual = date.today()

    dias_retraso = max((fecha_actual - fecha_limite).days, 0)
    multa = dias_retraso * MULTA_POR_DIA

    prestamo["estado"] = "Devuelto"
    prestamo["multa"] = round(multa, 2)

    for libro in libros:
        if libro["codigo"] == codigo_libro:
            libro["disponible"] = True
            break

    guardar_datos()

    return (
        f"Devolución registrada. Días de retraso: {dias_retraso}. "
        f"Multa: S/ {multa:.2f}"
    )


# Cargar los datos al iniciar el programa.
cargar_datos()