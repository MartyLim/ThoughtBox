from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from box import bcrypt
from box.models import User


class RegisterForm(FlaskForm):
	name = StringField('Name (optional)')

	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	password_confirm = PasswordField('Confirm Password', 
									validators=[DataRequired(), Length(max=20), EqualTo('password')])

	submit = SubmitField('Create Box')

	def validate_password(self, password):
		l = [i.password for i in User.query.all()]
		for i in l:
			if bcrypt.check_password_hash(i, password.data):
				raise ValidationError('Password not available')

class LoginForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Open Box')

class NoteForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])

	content = TextAreaField('Content', validators=[DataRequired()])

	submit = SubmitField('Add Note')
