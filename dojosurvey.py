from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'secret103048580e8w7'

# THE DEFAULT LANDING PAGE
@app.route("/")
def landing():
	return render_template("index.html")

@app.route("/result", methods = ["POST"])
def posting():
	if len(request.form['new_name']) < 1:
		flash("Name cannot be empty!") # just pass a string to the flash function
		return redirect("/")
	else:
		session['name'] = request.form['new_name']

	session['cars'] = request.form['cars']
	session['cars1'] = request.form['cars1']

	if len(request.form['comment']) < 1:
		flash("Comment cannot be empty!")
		return redirect("/")
	else:
		session['comment'] = request.form['comment']

	return redirect('/submitted')

@app.route("/submitted")
def submitted():
	return render_template(
		"submitted.html",
		name = session['name'],
		cars = session['cars'],
		cars1 = session['cars1'],
		comment = session['comment']
		)

app.run(debug=True)