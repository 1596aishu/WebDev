from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class User(db.Model):
   __tablename__ = 'USER'
   user = Column(String(150), primary_key=True)
   pwd = Column(String(100))   
