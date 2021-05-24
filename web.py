from flask import Flask
from flask import jsonify
from functions import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Append currency id in the url<you're currency id><br><pre>{'22':'AED','32':'ARS','1':'AUD','59':'BDT','37':'BND','35':'BRL','38':'BSD','15':'CAD','4':'CHF','17':'EUR','3':'GBP','20':'HKD','23':'ILS','29':'INR','56':'IQD','2':'JPY','115':'LKR','14':'MXN','129':'NPR','5':'NZD','75':'PKR',<br>'76':'QAR','79':'RUB','18':'SEK','19':'SGD','9':'TRY','12':'USD'}</pre>"

@app.route('/<curr_id>')
def newpage(curr_id):
    return jsonify(get_data(curr_id))

if __name__ == '__main__':
    app.run(host='localhost', port='80', debug=True)