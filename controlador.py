
import json
import modelo
import vista


def ejecutar() -> None:
    """Controla el funcionamiento general del sistema."""

    while True:
        vista.mostrar_menu()

        try:
            opcion = int(vista.pedir_dato("Seleccione una opción: "))

            if opcion == 1:
                codigo = vista.pedir_dato("Código del libro: ")
                titulo = vista.pedir_dato("Título del libro: ")
                autor = vista.pedir_dato("Autor del libro: ")

                if not codigo or not titulo or not autor:
                    vista.mostrar_mensaje(
                        "Todos los campos son obligatorios."
                    )
                    continue

                resultado = modelo.registrar_libro(
                    codigo, titulo, autor
                )
                vista.mostrar_mensaje(resultado)

            elif opcion == 2:
                codigo = vista.pedir_dato("Código del lector: ")
                nombre = vista.pedir_dato("Nombre del lector: ")

                if not codigo or not nombre:
                    vista.mostrar_mensaje(
                        "Todos los campos son obligatorios."
                    )
                    continue

                resultado = modelo.registrar_lector(codigo, nombre)
                vista.mostrar_mensaje(resultado)

            elif opcion == 3:
                libros = modelo.obtener_libros()
                vista.mostrar_libros(libros)

            elif opcion == 4:
                codigo_libro = vista.pedir_dato("Código del libro: ")
                codigo_lector = vista.pedir_dato("Código del lector: ")

                if not codigo_libro or not codigo_lector:
                    vista.mostrar_mensaje(
                        "Todos los campos son obligatorios."
                    )
                    continue

                resultado = modelo.registrar_prestamo(
                    codigo_libro, codigo_lector
                )
                vista.mostrar_mensaje(resultado)

            elif opcion == 5:
                codigo = vista.pedir_dato(
                    "Código del libro que se devolverá: "
                )

                if not codigo:
                    vista.mostrar_mensaje(
                        "Debe ingresar el código del libro."
                    )
                    continue

                resultado = modelo.registrar_devolucion(codigo)
                vista.mostrar_mensaje(resultado)

            elif opcion == 6:
                prestamos = modelo.obtener_prestamos()
                vista.mostrar_prestamos(prestamos)

            elif opcion == 7:
                vista.mostrar_mensaje(
                    "Gracias por utilizar el sistema."
                )
                break

            else:
                vista.mostrar_mensaje(
                    "Opción no válida. Intente nuevamente."
                )

        except (OSError, json.JSONDecodeError) as error:
            vista.mostrar_mensaje(
                f"Error al trabajar con los archivos: {error}"
            )

        except ValueError:
            vista.mostrar_mensaje("Ingrese un número válido.")

        except Exception as error:
            vista.mostrar_mensaje(
                f"Se produjo un error: {error}"
            )
