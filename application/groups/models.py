from application import db
from application.models import Base
from sqlalchemy.sql import text

class Group(Base):

    __tablename__ = "groups"

    name = db.Column(db.String(144), nullable=False)
    members = db.relationship("Member", backref='groups', lazy=True)

    def getId(self):
        return self.id

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_group_member_count():
        stmt = text("SELECT groups.id, groups.name, COUNT(member.id) "
            + "FROM groups LEFT JOIN member "
            + "ON member.group_id=groups.id "
            + "GROUP BY groups.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], 
                "name":row[1],
                "members":row[2]})
        
        return response

    @staticmethod
    def find_group_members(id):
        stmt = text("SELECT groups.id, groups.name, "
            + "member.id, member.firstnames, member.lastname "
            + "FROM groups LEFT JOIN member "
            + "ON member.group_id = groups.id "
            + "WHERE groups.id = :id "
            + "ORDER BY member.lastname"
            ).params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"group_id":row[0],
                "group_name":row[1],
                "member_id":row[2],
                "member_firstnames":row[3],
                "member_lastname":row[4]})
        
        return response
    
    @staticmethod
    def empty_group_count():
        res = db.engine.execute("SELECT COUNT(groups.id) as count "
            + "FROM groups WHERE groups.id NOT IN "
            + "(SELECT member.group_id FROM "
            + "member GROUP BY group_id)")
        
        for row in res:
            return row[0]
    
    @staticmethod
    def practices_per_group(id):
        stmt = text("SELECT COUNT(practice.id) "
            + "FROM practice WHERE practice.member_id IN "
            + "(SELECT member.id from member "
            + "WHERE member.group_id=:id)"
            ).params(id=id)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def group_coaches(id):
        stmt = text("SELECT member.lastname, member.firstnames, "
            + "member.phoneNumber FROM member "
            + "WHERE member.group_id=:id "
            + "AND member.id IN "
            + "(SELECT account.member_id FROM account "
            + "WHERE account.id IN "
            + "(SELECT role.user_id FROM role "
            + "WHERE role.name='ADMIN'))"
            ).params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"lastname":row[0],
                "firstnames":row[1],
                "phoneNumber":row[2]})
        
        return response