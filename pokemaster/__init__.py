from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

from pokemaster.pokedex import pokedex
app.register_blueprint(pokedex.bp)