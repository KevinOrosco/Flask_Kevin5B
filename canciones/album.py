from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('album', __name__, url_prefix='/album')

@bp.route("/album")
def albums():
    consulta1 = """
                SELECT Title, AlbumId FROM albums
                ORDER BY Title;
               """
    
    con = db.get_db()
    resultado = con.execute(consulta1)
    lista_de_albums = resultado.fetchall()
    pagina = render_template("album.html", albums = lista_de_albums)
    return pagina