from flask import Flask
from math import factorial

app = Flask(__name__)

@app.route('/')
def home():
    return 'Copie la siguiente URL y reemplace "n" por el número del factorial que desea ver: <br> http://127.0.0.1:5000/factorial/n'

@app.route('/factorial/<int:number>')
def calculate_factorial(number):
    try:
        result = factorial(number)
        return f'El factorial de {number} es {result}'
    except ValueError:
        return 'Debes ingresar un número menor, ya que el número ingresado es demasiado grande para calcular su factorial.'

if __name__ == '__main__':
    app.run(debug=True)
