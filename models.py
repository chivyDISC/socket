import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String, nullable = False)