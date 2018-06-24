from application import db
from application.models import Base
from application.groups.models import Group
from application.practice.models import Practice

from sqlalchemy.sql import text

class Grade(Base):
    name = db.Column(db.String(6), nullable=False)
    color = db.Column(db.String(20), nullable=False)

class Member(Base):
    firstnames = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144))
    phoneNumber = db.Column(db.String(20))
    address = db.Column(db.String(144))
    postalCode = db.Column(db.String(20))
    country = db.Column(db.String(20))
    city = db.Column(db.String(144))

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    group = db.relationship("Group")
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))
    grade = db.relationship("Grade")
    practices = db.relationship("Practice", cascade="all, delete, delete-orphan", backref='practice', lazy=True)

    def __init__(self, firstnames, lastname, group_id):
        self.firstnames = firstnames
        self.lastname = lastname
        self.group_id = group_id

    @staticmethod
    def find_members_with_group():
        stmt = text("SELECT groups.id, groups.name, "
            + "member.id, member.firstnames, "
            + "member.lastname, COUNT(practice.id) "
            + "FROM groups, member "
            + "LEFT JOIN practice "
            + "ON member.id = practice.member_id "
            + "WHERE groups.id=member.group_id "
            + "GROUP BY member.id, groups.id "
            + "ORDER BY member.lastname")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"groupId":row[0], "groupName":row[1], 
                "id":row[2], "firstnames":row[3],
                "lastname":row[4], "practiceCount":row[5]})
        
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