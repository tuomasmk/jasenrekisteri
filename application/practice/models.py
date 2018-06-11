from application import db
from application.models import Base
from sqlalchemy import UniqueConstraint

class Practice(Base):

    date = db.Column(db.Date, nullable=False, default=db.func.date())
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

    UniqueConstraint('date', 'member_id')
#    group_id = db.relationship("Group", backref='groups', lazy=True)
#    members = db.relationship("Member", 
#        secondary=practice_member_table,
#        backref="practices")


    def getId(self):
        return self.id

    def __str__(self):
        return self.id

    def __init__(self, date, member_id):
        self.date = date
        self.member_id = member_id

#practice_member_table = Table('practice_member_table', Base.metadata,
#    Column('practice_id', Integer, ForeignKey('practice_id')),
#    Column('member_id', Intger, ForeignKey('member_id'))
#)

#    practice_id = db.relationship("Practice", backref='practice', lazy=True)
#    member_id = db.relationship("Member", backref='member')