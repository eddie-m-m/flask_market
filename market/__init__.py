from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b42b4d6bb3553e0f6dbf8660'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
