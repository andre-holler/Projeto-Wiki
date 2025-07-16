from datetime import datetime
from app import db

class Wiki(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    texto = db.Column(db.String)
    data = db.Column(db.DateTime, default=datetime.now)