from app import db

class Wiki(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    titulo = db.Column(db.String)
    mensagem = db.Column(db.String)
    respostas = db.Column(db.Integer, default=0)
