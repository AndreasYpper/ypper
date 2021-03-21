from db import db
from werkzeug.security import generate_password_hash
from os import environ
import random


class UserModel(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(12))
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean)
    confirmed = db.Column(db.Boolean, default=False, server_default="false")
    confirmation_code = db.Column(db.Integer)
    confirmation_tries = db.Column(db.Integer, default=0, server_default="0")

    def __init__(self, first_name, last_name, email, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(
            password, method=environ.get("HASH_METHOD")
        )
        self.admin = False
        self.confirmed = False
        self.confirmation_code = random.randint(1000, 9999)
        self.confirmation_tries = 0

    def json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
        }

    def adminJson(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "admin": self.admin,
        }

    @classmethod
    def find_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()