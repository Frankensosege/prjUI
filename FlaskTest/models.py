from . import db

class Users(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    user_name = db.Column(db.VARCHAR(100), nullable=False)
    passwd = db.Column(db.VARCHAR(100), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    lastupdate_date = db.Column(db.DateTime(), nullable=False)