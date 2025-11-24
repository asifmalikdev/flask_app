from flask_sqlalchemy import SQLAlchemy
from .extentions import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)

    def __repr__(self):
        return f"<User {self.name}>"


class UserBooks(db.Model):
    __tablename__ = "userbooks"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    user = db.relationship("User", backref="books")

    def __repr__(self):
        return f"<Book {self.title}"
