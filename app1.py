import datetime
from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from sqlalchemy import create_engine, Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)
engine = create_engine('sqlite:///project.db')
db.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler, sign_up_handler
login_manager.init_app(app)

class User(db.Model):
    __tablename__  = 'user'
    id             = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String)
    email     = db.Column(db.String)
    password  = db.Column(db.String)
    location  = db.Column(db.String)
    birthday  = db.Column(db.String)
    bio       = db.Column(db.String)
    languages = db.Column(db.String)
    picture   = db.Column(db.String)
    # created_at = db.Column(db.DateTime, default=datetime.datetime.now())

class Journey(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String)
    Description = db.Column(db.String)
    picture     = db.Column(db.String)
    group_size  = db.Column(db.String)
    location    = db.Column(db.String)
    catagory    = db.Column(db.String)
    rate        = db.Column(db.String)
    creator     = db.Column(db.String)

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    # return login_handler(request)

    if request.method == 'GET':
        return render_template('sign_in.html')

    email = request.form['email']
    password = request.form['pw']
    if(session.query(User).filter_by(email = email).one()!= None and session.query(User).filter_by(email = email).one().check_password(password) and email != "" and password != ""):
        return redirect(url_for('home'))
    else:
        flash ("Email/Password is incorrect")
        return redirect(url_for('sign_in'))



@app.route('/logout')
def logout():
	return logout_handler()


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
	print (request.method)
	if request.method == 'GET':
		return render_template('sign_up.html')
	else:
		sign_up_handler(request)
		return redirect(url_for('home'))

if __name__=='__main__':
app.run(debug=True)

