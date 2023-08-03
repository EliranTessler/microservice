from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    salary_usd = db.Column(db.Float)

    def __init__(self, name, country, city, salary_usd):
        self.name = name
        self.country = country
        self.city = city
        self.salary_usd = salary_usd

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'city': self.city,
            'salary_usd': self.salary_usd
        }