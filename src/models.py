import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    firstname = Column(String(50), nullable=False)
    lasname = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}
    
class Media(Base):

    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(String (250))
    url = Column(String)
    post_id = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
