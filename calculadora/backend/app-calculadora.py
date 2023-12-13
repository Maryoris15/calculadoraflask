from flask import Flask
from flask_cors import CORS
import math as mt  
from flask import jsonify
app=Flask(__name__)
CORS(app)



@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
def suma(numero1=0,numero2=0):
    resultado=numero1+numero2
    data={
        "Resultado":resultado,
        "operacion":"suma",
     }
    return jsonify(data)
##RESTA

@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    data={
        "Resultado":resultado,
        "Operacion":"resta",
    }
    return jsonify(data)
##MULTIPLICACION
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicacion(numero1=0,numero2=0):
    resultado=numero1*numero2
    data={
        "Resultado":resultado,
        "Operacion":"multiplicación",
     }
    return jsonify(data)
##DIVISIÓN
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
def division(numero1=0,numero2=0):
    resultado=numero1/numero2
    data={
        "Resultado":resultado,
        "Operacion":"División",
    }
    return jsonify(data)

##potenciación

@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0,numero2=0):
    resultado=numero1**numero2
    data={
        "Resultado":resultado,
        "Operacion":"potenciación",
    }
    return jsonify(data)
##seno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado=mt.cos(numero1)
    data={
        "Resultado":resultado,
        "Operacion":"coseno",
    }
    return jsonify(data)
if __name__=='__main__':
    app.run(debug=True)





    