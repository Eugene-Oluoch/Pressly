#imports 
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

#Login Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




#User Database Model
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String,nullable=False)
    image_file = db.Column(db.String, nullable=False, default='default.jpeg')
    bio = db.Column(db.String)
    posts = db.relationship('Post', backref='users', lazy=True)


#Post Databse Model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String,nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)