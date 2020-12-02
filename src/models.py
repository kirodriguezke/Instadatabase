import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    email = Column(String)
    password = Column(String)


class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    date = Column(String)
    user = Column(String)

class post_likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('user.id'))
    published_at = Column(String)

class direct_message(Base):
    __tablename__ = 'direct_message'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('user.id'))
    recibed_id = Column(Integer, ForeignKey('user.id'))
    message = Column(String(300))
    published_at = Column(String)

class comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('user.id'))
    message = Column(String(300))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')