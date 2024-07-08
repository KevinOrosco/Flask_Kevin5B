from flask import Flask, render_template,Blueprint, request, redirect, url_for
from . import db

bp = Blueprint('artista', __name__, url_prefix='/artist')

@bp.route("/")
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
        SELECT Name FROM artists
        WHERE ArtistId = ? ;
    """
    consulta2 = """
        SELECT Title, AlbumId FROM albums
        WHERE ArtistId = ?;
    """
    res = con.execute(consulta1, (id, ))
    artista = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_albums = res.fetchall()
    pagina = render_template("detalle_artista.html",
                             artista = artista,
                             albums = lista_albums)
    return pagina

@bp.route("/new", methods=('GET', 'POST'))
def nuevo():
    if request.method == "POST":
        name = request.form("name")

        con = db.get_db()
        consulta = """ INSERT INTO artists(name)
        Values (?)
        """
        con.execute(consulta, (name, ))
        con.commit()
        return redirect(url_for("artist.artists"))
    else:
        pagina = render_template("new_artist.html")
        return pagina