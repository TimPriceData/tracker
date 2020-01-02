from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(64), index=False, unique=False)
    last_name = db.Column(db.String(64), index=False, unique=False)
    country = db.Column(db.String(64), index=True, unique=False)
    dob = db.Column(db.DateTime, index=True)
    logs = db.relationship('Log', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_start = db.Column(db.DateTime, index=True)
    time_stop = db.Column(db.DateTime, index=True)
    shallow = db.Column(db.Integer, index=True)
    concentrated = db.Column(db.Integer, index=True)
    deep = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User: {}>'.format(self.id)