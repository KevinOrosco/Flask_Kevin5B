from flask import Flask, render_template,Blueprint
from . import db

bp = Blueprint('artistas', __name__, url_prefix='/artist')

@bp.route("/artist")
def artistas():
    consulta1 = """
                SELECT Name, Artist_Id FROM artists
                ORDER BY Name;
               """
    consulta2 = """
                SELECT Name FROM genres
                ORDER BY Name;
               """
    consulta3 = """
                SELECT Name FROM Tracks
                ORDER BY Name;
               """
    
    con = db.get_db()
    resultado = con.execute(consulta1)
    lista_de_resultados = resultado.fetchall()
    resultado = con.execute(consulta2)
    lista_de_generos = resultado.fetchall()
    resultado = con.execute(consulta3)
    lista_de_canciones = resultado.fetchall()
    pagina = render_template("artist.html", artistas = lista_de_resultados, generos = lista_de_generos, canciones = lista_de_canciones)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Name, Artist_Id FROM artists
        WHERE Artist_Id = ? ;
    """
    consulta2 = """
        SELECT t.name, a.name, g.Title FROM tracks t
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