from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask

db = SQLAlchemy()

def init(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


class User(db.Model):
    id = Column('id', String(8), primary_key=True)

class Note(db.Model):
    id = Column('id', String(8), primary_key=True)
    author = Column('author', String(8))
    title = Column('title', UnicodeText(255))
    content = Column('content', UnicodeText(65535))