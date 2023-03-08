from flask import Flask

app = Flask(__name__)

@app.route('/cal/<int:num1>/<string:op>/<int:num2>')
def calculate(num1, op, num2):
    if op == 'add':
        result = num1 + num2
    elif op == 'subtract':
        result = num1 - num2
    elif op == 'multiply':
        result = num1 * num2
    elif op == 'modulus':
        result = num1 % num2
    else:
        return 'Invalid operation!'

    return f'Result: {result}'

if __name__ == '__main__':
    app.run(debug=True)
