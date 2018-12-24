from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 	
from flask_login import LoginManager

app = Flask(__name__)

#Used for securely signing the session cookie 
app.config['SECRET_KEY'] = 'fcd3809d42287aba80a933e44aaf082e'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


#import at bottom to prevent circle import problem
from box import routes