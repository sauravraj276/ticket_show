from .database import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.email)

    
class Show(db.Model):
    __tablename__ = 'show'
    show_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    tags = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

class Venue(db.Model):
    __tablename__ = 'venue'
    venue_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    place = db.Column(db.String, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)