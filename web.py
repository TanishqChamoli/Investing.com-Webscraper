from flask import Flask
from flask import jsonify
import internship

app = Flask(__name__)

@app.route('/')
def homepage():
    return jsonify(internship.fun())

if __name__ == '__main__':
    app.run(host='localhost', port='80', debug=True)