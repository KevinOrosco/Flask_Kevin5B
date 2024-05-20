from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

from . import artistas
app.register_blueprint(artistas.bp)