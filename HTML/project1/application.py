import os, sys, logging, time
import calendar
import time
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
import models
from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
db.query = db_session.query_property()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def init_db():
    db.metadata.create_all(bind=engine)
init_db()

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register", methods=["GET","POST"])
def response():
    if request.method == "POST":
        user = request.form.get("username")
        #print(id, file=sys.stdout)
        pwd = request.form.get("password")
        ch = USER.query.filter_by(username=user).first()
        if ch is not None:
            return render_template("register.html", headline=user+" Registered already. Login.")
        info = USER(username=user,password=pwd)
        db.session.add(info)
        db.session.commit()
        if len(user) == 0:
            user += "Please enter the details"
        else:
            user += " Registered. Please login."
        return render_template("register.html",headline=user)
    elif request.method == "GET":
        return render_template("register.html",headline="")

@app.route("/admin")
def database():
    users = USER.query.order_by(USER.timestamp).all()
    username = []
    password = []
    for i in users:
        username.append(i.username)
        password.append(i.password)
    return render_template("database.html", username=username,password=password,length=len(username))
