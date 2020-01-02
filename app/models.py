from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(64), index=False, unique=False)
    last_name = db.Column(db.String(64), index=False, unique=False)
    country = db.Column(db.String(64), index=True, unique=False)
    dob = db.Column(db.DateTime, index=True)
    logs = db.relationship('Log', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
