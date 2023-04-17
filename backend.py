from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api1', methods=["GET"])
def consultar():
    #return jsonify(list(range[5]))
    return "Texto de Retorno", 200


if __name__ == '__main__':
    app.run(port=5001, debug=True)