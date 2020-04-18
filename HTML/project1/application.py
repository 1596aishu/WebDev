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

logging.basicConfig(filename='logger.log',level=logging.DEBUG)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
db.query = db_session.query_property()
logging.debug("database sessions created")


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
        username = request.form.get("username")
        #print(id, file=sys.stdout)
        password = request.form.get("password")
        ch = USER.query.filter_by(username=username).first()
        if ch is not None:
            return render_template("registration.html", headline=username+" Registered already. Login.")
        info = USER(username=username,password=password,timestamp=calendar.timegm(time.gmtime()))
        db.session.add(info)
        db.session.commit()
        if len(username) == 0:
            username += "Please enter the details"
        else:
            username += " Registered. Please login."
        return render_template("registration.html",headline=username)
    elif request.method == "GET":
        return render_template("registration.html",headline="")

@app.route("/admin")
def database():
    users = USER.query.order_by(USER.timestamp).all()
    username = []
    password = []
    stamps = []
    for i in users:
        username.append(i.username)
        password.append(i.password)
        stamps.append(time.ctime(i.timestamp))
    return render_template("database.html", username=username,password=password,stamps=stamps,length=len(username))
