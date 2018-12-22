from flask import Flask, render_template, url_for
from forms import RegisterForm, LoginForm
app = Flask(__name__)

#Used for securely signing the session cookie 
app.config['SECRET_KEY'] = 'fcd3809d42287aba80a933e44aaf082e'

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

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/publicnotes")
def pub():
	return render_template('pub.html')

@app.route("/yournotes")
def pub():
	if loggedin:
		return render_template('your.html')
	else:
		return render_template('log in????')

@app.route("/register")
def register():
	form = RegisterForm()
	return render_template('register.html', title='Create a Box', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Open Your Box', form=form)


if __name__ == '__main__':
	app.run(debug=True)