from flask import Flask, request

app = Flask(__name__)


@app.route("/api")
def home():
    resultado = "Entre as notas da URL"

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:

        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = "Aprovado"
        elif media >= 4 and 7:
            resultado = "Recuperação"
        else:
            resultado = "Reprovado"

    return resultado


if __name__ == '__main__':
    app.run(port=5000, debug=True)