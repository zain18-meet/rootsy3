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


class User(db.Model):
    __tablename__  = 'user'
    id             = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    location = db.Column(db.String)
    birthday = db.Column(db.String)
    bio = db.Column(db.String)
    languages = db.Column(db.String)
    picture = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

class Journey(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    Description = db.Column(db.String)
    picture = db.Column(db.String)
    group_size = db.Column(db.String)
    location = db.Column(db.String)
    catagory = db.Column(db.String)

