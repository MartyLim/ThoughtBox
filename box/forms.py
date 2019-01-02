from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from box import bcrypt
from box.models import User


class RegisterForm(FlaskForm):
	name = StringField('Name (optional)')

	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])

	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	password_confirm = PasswordField('Confirm Password', 
									validators=[DataRequired(), Length(max=20), EqualTo('password')])

	submit = SubmitField('Create Box')

	def validate_username(self, password):
		yes = User.query.filter_by(username=username.data).first()
		if yes:
			raise ValidationError('Username not available')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(max=20)])

	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Open Box')

class NoteForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])

	content = TextAreaField('Content', validators=[DataRequired()])

	submit = SubmitField('Add Note')
