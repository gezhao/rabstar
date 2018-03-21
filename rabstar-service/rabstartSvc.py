
from flask import Flask
import json
from flask import request
from flask import make_response
from flask import render_template
import engine

import nlpservice

my_index = engine.Index()

app = Flask(__name__)

@app.route('/')
def rabstar():
	page = render_template('index.html')
	return page


@app.route('/search')

def search():
	q = request.args['q']
    	results = my_index.search(q)
    	return render_template("results.html", q=q, results=results)



# Return the JSON response based on req object
"""
def processRequest(req):   
    querymsg = req.get("queryMsg")
    context = req.get("session")
    insight=nlpservice.callnlp(querymsg, context)
    res=makeRabstarResult(insight)
    return res



## Get the nlpInsight json and genearte the return message json as knowledge bot
def makeRabstarResult(nlpInsight):

	data = {"respMsg":"test", "session":"test2"}
	return data
"""
if __name__ == "__main__":
	app.run(debug=True)

