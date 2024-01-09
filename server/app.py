#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)  # Initialize db with your Flask app

migrate = Migrate(app, db)  # Initialize migration with your Flask app and db

if __name__ == '__main__':
    app.run(port=5555)
