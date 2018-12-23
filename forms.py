from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])

	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	password_confirm = PasswordField('Confirm Password', 
									validators=[DataRequired(), Length(max=20), EqualTo('password')])

	submit = SubmitField('Create Box')

class LoginForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Open Box')



