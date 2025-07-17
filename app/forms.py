from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import db
from app.models import Wiki

class WikiForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    texto = StringField('Texto', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        wiki = Wiki(
            titulo = self.titulo.data,
            texto = self.texto.data,
            id_user = user_id
        )
    
        db.session.add(wiki)
        db.session.commit