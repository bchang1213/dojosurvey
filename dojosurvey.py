from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'secret103048580e8w7'

# THE DEFAULT LANDING PAGE
@app.route("/")
def landing():
		return render_template("index.html")

@app.route("/result", methods = ['POST'])
def posting():
	return render_template("submitted.html",name = request.form['new_name'], cars = request.form['cars'], cars1 = request.form['cars1'], comment = request.form['comment'])

app.run(debug=True)