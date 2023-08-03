#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from decouple import config
from api.models.employee_model import db
from flask_sqlalchemy import SQLAlchemy
from api.routes.employee_routes import employee_ms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')

db.init_app(app)

app.register_blueprint(employee_ms)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)
