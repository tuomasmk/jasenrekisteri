from application import db
from application.models import Base
from application.groups.models import Group
from application.practice.models import Practice

from sqlalchemy.sql import text

class Member(Base):
    
    firstnames = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    practices = db.relationship("Practice", backref='practice', lazy=True)
#    practices = db.relationship("Practice",
#        secondary=practice_member_table,
#        back_populates="Members")

    def __init__(self, firstnames, lastname, group_id):
        self.firstnames = firstnames
        self.lastname = lastname
        self.group_id = group_id

    @staticmethod
    def find_members_with_group():
        stmt = text("SELECT Member.id, Member.firstnames, "
            + "Member.lastname, Groups.name FROM Member, Groups "
            + "WHERE Member.group_id=Groups.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            print(row[0])
            print(row[1])
            response.append({"id":row[0], "firstnames":row[1], 
                "lastname":row[2], "groupName":row[3]})
        
        return response

    @staticmethod
    def find_member_and_practices(id):
        stmt = text("SELECT Member.id, Member.firstnames, Member.lastname, "
            + "COUNT(Practice.id) FROM Member "
            + "LEFT JOIN Practice ON Member.id = Practice.member_id "
            + "WHERE Member.id = :id "
            ).params(id=id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id":row[0], "firstnames":row[1],
                "lastname":row[2], "practiceCount":row[3]})
        
        return response