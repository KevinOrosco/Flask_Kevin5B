from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('album', __name__, url_prefix='/album')

@bp.route("/")
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

@bp.route("/<int:id>")
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Title FROM albums
        WHERE AlbumId = ?;
    """
    consulta2 = """
        SELECT name, TrackId FROM tracks 
        WHERE AlbumId = ? ;
    """
    res = con.execute(consulta1, (id, ))
    albums = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_canciones = res.fetchall()
    pagina = render_template("detalle_album.html"
                             , album = albums,
                               canciones = lista_canciones)
    return pagina