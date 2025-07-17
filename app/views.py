from app import app
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user
from app.forms import UserForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        if form.validate_email():
            user = form.save()
            login_user(user, remember=True)
            return redirect(url_for('homepage'))
        else:
            return
    return render_template('cadastro.html', form=form)
