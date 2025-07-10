from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class Comentario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    titulo = StringField('Título', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])