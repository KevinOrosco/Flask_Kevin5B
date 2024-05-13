from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route("/artist")
def artistas():
    consulta1 = """
                SELECT Name FROM artists
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