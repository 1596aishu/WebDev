from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class USER(db.Model):
   __tablename__ = 'USER'
   username = Column(String(50), primary_key=True)
   password = Column(String(50))  
   timestamp = Column(Integer, nullable=False) 
   def __init__(self, username, password, timestamp):
      self.username = username
      self.password = password
      self.timestamp = timestamp
   def __repr__(self):
      return '<User %r>' % (self.username)
