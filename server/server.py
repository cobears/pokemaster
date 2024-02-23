from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return jsonify({
        'message': "Hello World!",
        'pokemon': ['charmander', 'squirtle', 'bulbasaur']
        }
    )


@app.route("/api/pokedex", methods=['GET'])
def pokedex():
    return jsonify({
        'message': "Hello World!",
        'pokemon': ['charmander', 'squirtle', 'bulbasaur']
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)

