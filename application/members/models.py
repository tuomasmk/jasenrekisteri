from application import db
from application.groups.models import Group

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    firstnames = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    def __init__(self, firstnames, lastname, group_id):
        self.firstnames = firstnames
        self.lastname = lastname
        self.group_id = group_id
