from flask import Flask, render_template, flash, url_for, redirect
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
app = Flask(__name__)

#Used for securely signing the session cookie 
app.config['SECRET_KEY'] = 'fcd3809d42287aba80a933e44aaf082e'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False, default='anonymous')
	password = db.Column(db.String(20), unique=True, nullable=False)

	notes = db.relationship('Note', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.name}', '{self.password}')"

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Note('{self.title}', '{self.date_posted}')"


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


if __name__ == '__main__':
	app.run(debug=True)