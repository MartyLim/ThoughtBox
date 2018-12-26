from flask import render_template, flash, url_for, redirect
from box.forms import RegisterForm, LoginForm, NoteForm
from box.models import User, Note
from box import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    return render_template('home.html')


@app.route("/publicnotes")
def pub():
	return render_template('pub.html', title='Public', notes=notes)

@app.route("/yournotes")
@login_required
def your():
	if current_user.is_authenticated:
		return render_template('your.html', title='Notes')
	else: 
		return redirect(url_for('login'))

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		x = ""
		if form.name.data == "":
			x = "anonymous"
			flash(f'Box created for "anonymous"! Open your new box', 'success')
		else:
			x = form.name.data
			flash(f'Box created for "{form.name.data}"! Open your new box', 'success')
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		newuser = User(name=x, password=hashed_pass)
		db.session.add(newuser)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Create', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		l = [i.password for i in User.query.all()]
		for i in l:
			if bcrypt.check_password_hash(i, form.password.data):
				user = User.query.filter_by(password=i).first()
				login_user(user, remember=form.remember.data)
				return redirect(url_for('your'))
		flash('Box Not Found', 'danger')
	return render_template('login.html', title='Open', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('hello'))

@app.route("/newnote", methods=['GET', 'POST'])
@login_required
def new_note():
	form = NoteForm()
	if form.validate_on_submit():
		flash(f'Note has been added to your Box!', 'success')
		return redirect(url_for('your'))
	return render_template('newnote.html', title='Note', form=form)