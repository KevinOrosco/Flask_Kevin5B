from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route("/artist")
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