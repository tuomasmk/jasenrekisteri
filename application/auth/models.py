from application import db
from application.models import Base
from sqlalchemy import UniqueConstraint

class Role(Base):
	name = db.Column(db.String(20), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

class User(Base):

	__tablename__ = "account"

	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)
	userRoles = db.relationship("Role", cascade="all, delete, delete-orphan", backref='role', lazy=True)
	
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
	member = db.relationship("Member")

	UniqueConstraint('username')

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password = password

	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	def roles(self):
		roles = Role.query.filter_by(user_id=self.id)
		roleNames = []
		for role in roles:
			roleNames.append(role.name)

		return roleNames