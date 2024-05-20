from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('artista', __name__, url_prefix='/artist')

@bp.route("/artist")
def artistas():
    consulta1 = """
                SELECT Name, ArtistId FROM artists
                ORDER BY Name;
               """
    
    con = db.get_db()
    resultado = con.execute(consulta1)
    lista_de_resultados = resultado.fetchall()
    pagina = render_template("artist.html", artistas = lista_de_resultados)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Name, ArtistId FROM artists
        WHERE ArtistId = ? ;
    """
    consulta2 = """
        SELECT t.name, g.Title FROM tracks t
        JOIN albums g ON t.AlbumId = g.AlbumId
        JOIN artists a ON g.ArtistId = a.ArtistId
        WHERE a.ArtistId = ? ;
    """
    res = con.execute(consulta1, (id, ))
    artista = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_canciones = res.fetchall()
    pagina = render_template("detalle_artista.html",
                             artista = artista,
                             canciones = lista_canciones)
    return pagina