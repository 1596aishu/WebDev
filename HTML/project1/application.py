import os, sys, logging, time
import calendar
import time
from flask_login import LoginManager, login_user , logout_user , current_user , login_required
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

import models
from models import BOOK, USER, Base
# from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)
<<<<<<< HEAD
# db.init_app(app)
=======
db.init_app(app)
>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
<<<<<<< HEAD
Base.query = db.query_property()
Base.metadata.create_all(bind=engine)
# sess = db()

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

=======
sess = db()

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096
# def init_db():
#     db.metadata.create_all(bind=engine)
# init_db()

@app.route("/")
def index():
    if request.method == "GET":
        if session.get("username") is not None:
            return render_template("index.html", headline= session["username"])
        return render_template("registration.html",headline="")


@app.route("/register", methods=["GET","POST"])
def response():
    if request.method == "POST":
        username = request.form.get("username")
        #print(id, file=sys.stdout)
        password = request.form.get("password")
        # ch = USER.query.filter_by(username=username).first()
        # if ch is not None:
        #     return render_template("registration.html", headline=username+" Registered already. Login.")
        info = USER(username=username,password=password,timestamp=calendar.timegm(time.gmtime()))
        try:
<<<<<<< HEAD
            db.add(info)
            db.commit()
=======
            sess.add(info)
            sess.commit()
>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096
            username += " registered. Please login."
            return render_template("registration.html",headline=username)
        except:
            text ="Account already exists!please try again with new account or login"
            return render_template("registration.html",headline=text)
<<<<<<< HEAD
    elif request.method == "GET":
        return render_template("registration.html",headline="")



@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "POST":
        word = request.form['searchbox']
        choice = request.form['choice']
        if choice == "isbn":
            # query = Book.query.filter(Book.isbn == word)
            # result = Book(isbn = )
            query = BOOK.query.filter(BOOK.isbn.like('%word%'))
        elif choice == "bname":
            # query = Book.query.filter(Book.bname == word)
            query = BOOK.query.filter(BOOK.bname.like('%word%'))
        else:
            # query = Book.query.filter(Book.author == word)
            query = BOOK.query.filter(BOOK.author.like('%word%'))
        # result = db.session.execute(query)
        for row in query:
            strs += "isbn: "+ row.isbn+ " book name: "+ row.bname+ " Author: "+ row.author
        return strs
        
    elif request.method == "GET":
        return render_template("registration.html",headline="")


=======
    elif request.method == "GET":
        return render_template("registration.html",headline="")

>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096
@app.route("/auth", methods=["GET","POST"])
def authentication():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
<<<<<<< HEAD
        query = db.query(USER).filter_by(username=username)
        if query is None:
            return render_template("registration.html", headline="WRONG CREDENTIALS")
        # query = USER.query.filter(USER.username.in_([username]), USER.password.in_([password]))
        # result = query.first()
        else:
            print(query)
            session["username"] = username
            return render_template("search.html", headline=" welcome "+session["username"])
        
=======
        query = USER.query.filter(USER.username.in_([username]), USER.password.in_([password]) )
        # result = query.first()
        if query:
            session["username"] = username
            return render_template("index.html", headline=" welcome "+session["username"])
        return render_template("registration.html", headline="WRONG CREDENTIALS")
>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096
    elif request.method == "GET":
        return redirect("register")

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



@app.route("/logout", methods=["GET","POST"])
def logout():
    session.clear()
<<<<<<< HEAD
    return redirect("/")
=======
    return redirect("/")
    
>>>>>>> b704b855c96ada10b58e7e0963ccb6e3e16cd096
