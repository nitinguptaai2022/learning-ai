from flask import  Flask , request , jsonify

app = Flask(__name__)


@app.route('/MySumFunction', methods=['GET', 'POST'])
def test():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/MySumFunction/Divide', methods=['POST'])
def test1():
    if (request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a/b
        return jsonify(str(result))

@app.route('/MySumFunction/Multiply', methods=['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a*b
        return jsonify(str(result))

@app.route('/Function/Concat', methods=['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['sudh']
        b = request.json['kumar']
        result = a+b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run()
