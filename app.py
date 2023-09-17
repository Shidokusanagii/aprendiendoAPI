from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return jsonify({'message': 'Hola, esta es mi API en Python!'})

if __name__ == '__main__':
    app.run(debug=True)