from application import db

class Group(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

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
