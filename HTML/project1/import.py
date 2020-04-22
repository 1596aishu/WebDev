import os
import csv
import sys
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from models import BOOK, USER, Base

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
Base.query = db.query_property()
Base.metadata.create_all(bind=engine)

# db.init_app(app)

def main():
    with app.app_context():
        # db.create_all()
        f = open("books.csv")
        read = csv.reader(f)
        for isbn, bname, author, year in read:
            info = BOOK(isbn=isbn, bname=bname, author=author, year=year)
            db.add(info)
            db.commit()
        print("All fields successfully added", file=sys.stdout)

if __name__ == "__main__":
    main()