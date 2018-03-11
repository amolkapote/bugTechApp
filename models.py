'''
    @author: AK
    @summary: model object for ORM
        this will create two database tables Contact and Bug in bugs.sqlite
'''


from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# this will create a database in same folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Object
class Contact(db.Model):


    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return '<Contacts %r>' % self.name

# Bug object
class Bug(db.Model):
    __tablename__ = 'bugs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    # this will add default date, bug creation date
    date = db.Column(db.String(20), nullable=False, server_default=datetime.now().strftime('%m/%d/%Y'))#Column(DateTime(timezone=True), server_default=func.now())
    user = db.Column(db.String(100), nullable=False)
    #user = db.orm.relationship(Bug, backref='locations')
    status = db.Column(db.String(10), nullable=False)
    
    
    def __repr__(self):
        return '<Bugs %r>' % self.title


