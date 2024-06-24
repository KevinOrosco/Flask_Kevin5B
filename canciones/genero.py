from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route("/genero")
def generos():
    consulta1 = """
                SELECT Name, GenreId FROM genres
                ORDER BY Name;
               """
    
    con = db.get_db()
    resultado = con.execute(consulta1)
    lista_de_generos = resultado.fetchall()
    pagina = render_template("genero.html", generos = lista_de_generos)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT GenreId, name FROM genres
        WHERE GenreId = ?;
    """
    consulta2 = """
        SELECT t.name AS nombre, g.name FROM tracks t
        JOIN genres g ON t.GenreId = g.GenreId
        WHERE g.GenreId = ?;
    """
    res = con.execute(consulta1, (id, ))
    genero = res.fetchone()
    res = con.execute(consulta2, (id, ))
    canciones_genero = res.fetchall()
    pagina = render_template("detalle_genero.html",
                             genero = genero,
                             canciones_genero = canciones_genero)
    return pagina