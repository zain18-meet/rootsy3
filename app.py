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