from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('artistas', __name__, url_prefix='/artist')

@bp.route("/artist")
def artistas():
    consulta = """
                SELECT Name FROM artists
                ORDER BY Name;
               """
    
    con = db.get_db()
    resultado = con.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("artist.html", artistas = lista_de_resultados)
    return pagina