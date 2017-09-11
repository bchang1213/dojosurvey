from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secret103048580e8w7'

# THE DEFAULT LANDING PAGE
@app.route("/")
def landing():
		return render_template("index.html")

@app.route("/result", methods = ['POST'])
def posting(**kwargs):
	request.form['new_name']
	request.form['cars']
	request.form['cars1']
	request.form['comment']
	return render_template("submitted.html")

app.run(debug=True)