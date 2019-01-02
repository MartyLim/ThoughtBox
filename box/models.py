from datetime import datetime
from box import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False, default='anonymous')
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(20), unique=False, nullable=False)

	notes = db.relationship('Note', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.name}', '{self.username}')"

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Note('{self.title}', '{self.date_posted}')"