from datetime import datetime
from app import db
from flask_login import UserMixin

class Wiki(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    texto = db.Column(db.String)
    data = db.Column(db.DateTime, default=datetime.now)

    #Foreign Keys
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #Relacionamento
    comentarios = db.relationship('Comentario', backref='wiki', lazy=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)

    #Relacionamentos
    wikis = db.relationship('Wiki', backref='id_user', lazy=True)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String)

    #Foreign Keys
    id_user = db.Column(db.Integer, db.ForeignKey('user.id' ), nullable=False)
    id_wiki = db.Column(db.Integer, db.ForeignKey('wiki.id'), nullable=False)
    id_comentario = db.Column(db.Integer, db.ForeignKey('comentario.id'), nullable=True)

    #Relacionamento
    resposta_comentarios = db.relationship('Comentario', backref='comentario_id', lazy=True)