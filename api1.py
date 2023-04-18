from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Api Teste"

@app.route('/camiseta')
def text():
    return "Vem comprar camiseta da Largatixa"
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)