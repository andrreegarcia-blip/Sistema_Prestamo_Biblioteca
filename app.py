
from flask import Flask, render_template, redirect, request
import modelo

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/libros")
def libros():
    lista_libros = modelo.obtener_libros()
    return render_template("libros.html", libros=lista_libros)


@app.route("/eliminar_libro/<codigo>")
def eliminar_libro(codigo):
    modelo.eliminar_libro(codigo)
    return redirect("/libros")


@app.route("/registrar_libro", methods=["POST"])
def registrar_libro():
    codigo = request.form["codigo"]
    titulo = request.form["titulo"]
    autor = request.form["autor"]

    modelo.registrar_libro(codigo, titulo, autor)

    return redirect("/libros")


@app.route("/lectores")
def pagina_lectores():
    lista_lectores = modelo.obtener_lectores()
    return render_template("lectores.html", lectores=lista_lectores)


@app.route("/registrar_lector", methods=["POST"])
def registrar_lector():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]

    modelo.registrar_lector(codigo, nombre)

    return redirect("/lectores")


@app.route("/prestamos")
def pagina_prestamos():
    lista_prestamos = modelo.obtener_prestamos()
    lista_libros = modelo.obtener_libros()
    lista_lectores = modelo.obtener_lectores()

    return render_template(
        "prestamos.html",
        prestamos=lista_prestamos,
        libros=lista_libros,
        lectores=lista_lectores
    )


@app.route("/registrar_prestamo", methods=["POST"])
def registrar_prestamo():
    codigo_libro = request.form["codigo_libro"]
    codigo_lector = request.form["codigo_lector"]

    modelo.registrar_prestamo(codigo_libro, codigo_lector)

    return redirect("/prestamos")


@app.route("/devoluciones")
def pagina_devoluciones():
    lista_prestamos = modelo.obtener_prestamos()

    return render_template(
        "devoluciones.html",
        prestamos=lista_prestamos
    )


@app.route("/registrar_devolucion", methods=["POST"])
def registrar_devolucion():
    codigo_libro = request.form["codigo_libro"]

    modelo.registrar_devolucion(codigo_libro)

    return redirect("/devoluciones")


if __name__ == "__main__":
    app.run(debug=True)
