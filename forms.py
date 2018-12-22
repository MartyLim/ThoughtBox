from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	password_confirm = PasswordField('Confirm Password', 
									validators=[DataRequired(), Length(max=20), EqualTo('password')])

	submit = SubmitField('Get Started!')

class LoginForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Open Box')

