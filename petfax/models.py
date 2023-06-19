from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fact(db.Model):
    tablename = 'facts'

    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(30))
    fact = db.Column(db.Text)