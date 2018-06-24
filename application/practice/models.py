from application import db
from application.models import Base
from sqlalchemy import UniqueConstraint

class Practice(Base):

    date = db.Column(db.Date, nullable=False, default=db.func.date())
    duration = db.Column(db.Integer, default=60)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

    UniqueConstraint('date', 'member_id')

    def getId(self):
        return self.id

    def __str__(self):
        return self.id

    def __init__(self, date, member_id):
        self.date = date
        self.member_id = member_id