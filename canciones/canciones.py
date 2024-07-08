from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("canciones",__name__, url_prefix="/canciones")

@bp.route('/')
def canciones():
    consulta1 = """
            SELECT name FROM tracks
          """
    con = db.get_db()

    resultado = con.execute(consulta1)
    lista_de_canciones = resultado.fetchall()

    pagina = render_template("cancion.html", canciones=lista_de_canciones)
    return pagina


@bp.route("/<int:id>")
def detalle(id):
    consulta1 = """
        SELECT Name FROM tracks
        WHERE TrackId = ?
    """
    
    con = db.get_db()
    resultado = con.execute(consulta1, (id, ))
    cancion = resultado.fetchone()


    pagina = render_template("detalle_cancion.html", cancion = cancion)
    return pagina