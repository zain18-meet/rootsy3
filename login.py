from flask import redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user

import sys

from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager()

############# NOTE !! CHANGE URLS ###############
@login_manager.user_loader
def load_user(user_id):
    user = session.query(User).filter_by(id=user_id)
    if user.count() == 0:
        return
    return user.first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


def login_handler(request):
    if request.method == 'GET':
        return render_template('sign_in.html')

    email = request.form.get('email')
    pw    = request.form.get('pw')
    user  = session.query(User).filter_by(email=email) 
    if user.count() == 1:
        user = user.first()
        if user.check_password(pw):
            login_user(user)
            return redirect(url_for('home'))
        flash('Wrong Password')
    flash('Bad login')


def logout_handler():
    logout_user()
    return 'Logged out'


def sign_up_handler(request):
    new_first_name    = request.form.get('firstname')
    new_email         = request.form.get('email')
    new_last_name     = request.form.get('lastname')
    new_pass          = request.form.get('pass')
    new_photo         = request.form.get('photo')
    new_user = User(
        first_name=new_first_name,
        email=new_email,
        last_name= new_last_name,
        photo=new_photo
    )
    new_user.set_password(new_pass)
    session.add(new_user)        
    session.commit()
login_user(new_user)