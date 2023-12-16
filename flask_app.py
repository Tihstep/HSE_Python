from flask import Flask, jsonify, request
from Calculator import Calculator

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calculate():
    expression = request.get_json()['expression']
    try:
        calculator = Calculator()
        result = calculator.evaluate(expression)
        return jsonify({'input': expression, 'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
    print(1)