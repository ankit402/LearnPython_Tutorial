from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# Create db instance
db = SQLAlchemy()
# Create blueprint
mydb_bp = Blueprint('mydb', __name__)


# Example model
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    age = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    #modify the business logic
    address = db.Column(db.String(200), nullable=False)


    def __init__(self, username, password, age, gender, phone, email, address):
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(100), unique=True, nullable=False)
    groupdescription = db.Column(db.String(200))

    def __init__(self, groupname,groupdescription):
        self.groupname = groupname
        self.groupdescription = groupdescription

class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100), unique=True, nullable=False)
    groupid = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, userid,groupid):
        self.userid = userid
        self.groupid = groupid

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Rolename = db.Column(db.String(100), unique=True, nullable=False)
    RoleDescription = db.Column(db.String(200))

    def __init__(self, Rolename,RoleDescription):
        self.rolename = Rolename
        self.RoleDescription = RoleDescription

def add_column():
    with db.engine.connect() as conn:
        conn.execute(
            text("ALTER TABLE User COLUMN ADD COLUMN address TEXT")
        )
        print("Column renamed successfully!")