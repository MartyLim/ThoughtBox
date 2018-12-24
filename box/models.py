from datetime import datetime
from box import db

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