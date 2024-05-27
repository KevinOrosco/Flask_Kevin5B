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