
def mostrar_menu() -> None:
    """Muestra las opciones principales del sistema."""
    print("\n====================================")
    print("   SISTEMA DE PRÉSTAMO DE LIBROS")
    print("====================================")
    print("1. Registrar libro")
    print("2. Registrar lector")
    print("3. Consultar libros")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Ver préstamos")
    print("7. Salir")
    print("====================================")


def pedir_dato(mensaje: str) -> str:
    """Solicita un dato y elimina espacios sobrantes."""
    return input(mensaje).strip()


def mostrar_mensaje(mensaje: str) -> None:
    """Muestra un mensaje en pantalla."""
    print("\n" + mensaje)


def mostrar_libros(libros: list) -> None:
    """Muestra los libros registrados."""
    print("\n========== LISTA DE LIBROS ==========")

    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"

        print(f"Código: {libro['codigo']}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Estado: {estado}")
        print("------------------------------------")


def mostrar_prestamos(prestamos: list) -> None:
    """Muestra los préstamos registrados."""
    print("\n========== LISTA DE PRÉSTAMOS ==========")

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for prestamo in prestamos:
        print(f"Libro: {prestamo['codigo_libro']}")
        print(f"Lector: {prestamo['codigo_lector']}")
        print(f"Fecha de préstamo: {prestamo['fecha_prestamo']}")
        print(f"Fecha de devolución: {prestamo['fecha_devolucion']}")
        print(f"Estado: {prestamo['estado']}")
        print(f"Multa: S/ {prestamo['multa']:.2f}")
        print("---------------------------------------")
