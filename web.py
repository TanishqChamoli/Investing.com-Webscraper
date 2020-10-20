from flask import Flask
from flask import jsonify
import ape
import para_scrape

app = Flask(__name__)

@app.route('/')
def homepage():
    return jsonify(ape.fun())

@app.route('/new/<curr_id>')
def newpage(curr_id):
    return jsonify(para_scrape.fun(curr_id))

if __name__ == '__main__':
    app.run(host='localhost', port='80', debug=True)