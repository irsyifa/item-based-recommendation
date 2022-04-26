from flask_mongoengine import MongoEngine, Document
from bootstrap.extensions import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Rating(db.Document):
    meta = {'collection': 'ratings'}
    userId = db.StringField()
    itemId = db.IntField()
    rating = db.FloatField()

class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    username = db.StringField()
    password_hash = db.StringField()
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

