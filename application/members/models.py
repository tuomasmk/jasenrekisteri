from application import db
from application.models import Base
from application.groups.models import Group
from application.practice.models import Practice

from sqlalchemy.sql import text

class Member(Base):
    
    firstnames = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    practices = db.relationship("Practice", cascade="all, delete, delete-orphan", backref='practice', lazy=True)
#    practices = db.relationship("Practice",
#        secondary=practice_member_table,
#        back_populates="Members")

    def __init__(self, firstnames, lastname, group_id):
        self.firstnames = firstnames
        self.lastname = lastname
        self.group_id = group_id

    @staticmethod
    def find_members_with_group():
        stmt = text("SELECT member.id, member.firstnames, "
            + "member.lastname, groups.name FROM member, groups "
            + "WHERE member.group_id=groups.id")
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
        stmt = text("SELECT member.id, member.firstnames, member.lastname, "
            + "COUNT(practice.id) FROM member "
            + "LEFT JOIN practice ON member.id = practice.member_id "
            + "WHERE member.id = :id GROUP BY member.id"
            ).params(id=id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"id":row[0], "firstnames":row[1],
                "lastname":row[2], "practiceCount":row[3]})
        
        return response

    @staticmethod
    def find_practices_for_member(id):
        stmt = text("SELECT practice.id, practice.date "
                    + "FROM practice, member "
                    + "WHERE practice.member_id = member.id "
                    + "AND member.id = :id "
                    + "ORDER BY practice.date DESC"
                    ).params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],
                "date":row[1]})
        
        return response