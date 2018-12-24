from flask import render_template, flash, url_for, redirect
from box.forms import RegisterForm, LoginForm
from box.models import User, Note
from box import app

notes = [
	{
		'name':'Martin Lim',
		'title':'project ideas',
		'content':'quick note taking web application',
		'date':'12-20-2018'
	},
	{
		'name':'John Doe',
		'title':"grocery list",
		'content':'apples, tuna, chocolate',
		'date':'12-21-2018'
	}
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', notes=notes)


@app.route("/publicnotes")
def pub():
	return render_template('pub.html')

@app.route("/yournotes")
def your():
	return render_template('your.html')
	'''
	if loggedin:
		return render_template('your.html')
	elif boolean field?? or something to differentiate the stuff idk ???? ------ >>>>> 
		return render_template('login.html')
	'''

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		if list({form.name.data})[0] == "":
			flash(f'Box created for "anonymous"!', 'success')
		else:
			flash(f'Box created for "{form.name.data}"!', 'success')
		return redirect(url_for('your'))
	return render_template('register.html', title='Create', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#For testing purposes
		if form.password.data == 'password':
			flash(f'Your Box Has Been Retrieved!', 'success')
			return redirect(url_for('your'))
		else:
			flash('Box Not Found', 'danger')
	return render_template('login.html', title='Open', form=form)