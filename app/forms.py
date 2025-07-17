from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app import db, bcrypt
from app.models import Wiki, User

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

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao = PasswordField('Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit=SubmitField('Enviar')
    
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            return ValidationError('Usuário já cadastrado com esse E-mail!!!')
    
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            email = self.email.data,
            senha = senha
        )

        db.session.add(user)
        db.session.commit()
        return user
    
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            else:
                raise Exception("Senha incorreta!")
        else:
            raise Exception("Usuário não encontrado!")