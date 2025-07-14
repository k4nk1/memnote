from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, UnicodeText, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask import Flask

db = SQLAlchemy()

def init(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[str] = mapped_column(String(22), primary_key=True)
    notes: Mapped[list['Note']] = relationship(back_populates='author')

class Note(db.Model):
    __tablename__ = 'note'  
    id: Mapped[str] = mapped_column(String(22), primary_key=True)
    author: Mapped['User'] = relationship(back_populates='notes')
    author_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str] = mapped_column(UnicodeText(255))
    content: Mapped[str] = mapped_column(UnicodeText(65535))