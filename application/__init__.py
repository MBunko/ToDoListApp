from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.246.7.94/todo"

db = SQLAlchemy(app)

from application import routes