from . import db
import datetime
# from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    
    __tablename__ = 'user_profile'

    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String(120))
    
    last_name = db.Column(db.String(150))
    
    gender = db.Column(db.String(40))
    
    email = db.Column(db.String(250))
    
    location = db.Column(db.String(300))
    
    biography = db.Column(db.String(450))
    
    photo = db.Column(db.String(120))
    
    # user_created = db.Column(db.String(50), unique=True)
    
    user_created = db.Column(db.DateTime, default=datetime.datetime.utcnow()) 
    

    def __init__(self, first_name, last_name, gender, email, location, biography, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo =photo
        # self.user_created = user_created
        
        # datetime.datetime.utcnow().strftime("%d %m %Y")
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
