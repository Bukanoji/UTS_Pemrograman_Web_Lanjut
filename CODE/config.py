from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
# Initialize app and database connection
app = Flask(__name__)
# Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://oji:oji@localhost/oji'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()