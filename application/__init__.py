from flask import Flask
app = Flask(__name__)

#database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


#login
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

from application import views

from application.members import models
from application.members import views

from application.groups import models
from application.groups import views

from application.practice import views

from application.auth import models
from application.auth import views

from application.auth.models import User
from application.auth.models import Role
from application.members.models import Grade

@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(user_id)

#create db if it does not exist
from sqlalchemy.sql import text
try:
    db.create_all()
    if not os.environ.get("HEROKU"):
        if db.session.query(User.id).filter_by(name='testi').scalar() is None:
            db.engine.execute(text("INSERT INTO account "
                + "(name, username, password) "
                + "VALUES ('testi', 'testi', 'testi')"))
        admin_id = db.session.query(User.id).filter_by(name='admin').scalar()
        if admin_id is None:
            db.engine.execute(text("INSERT INTO account "
                + "(name, username, password) "
                + "VALUES ('admin', 'admin', 'admin')"))
        if db.session.query(Role.id).filter_by(user_id=admin_id).scalar() is None:
            db.engine.execute(text("INSERT INTO role "
                + "(name, user_id) "
                + "VALUES ('ADMIN', :id)")
                .params(id=admin_id))
    if db.session.query(Grade.id).filter_by(name='6.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('6.kyu', 'white')")
    if db.session.query(Grade.id).filter_by(name='5.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('5.kyu', 'yellow')")
    if db.session.query(Grade.id).filter_by(name='4.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('4.kyu', 'orange')")
    if db.session.query(Grade.id).filter_by(name='3.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('3.kyu', 'green')")
    if db.session.query(Grade.id).filter_by(name='2.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('2.kyu', 'blue')")
    if db.session.query(Grade.id).filter_by(name='1.kyu').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('1.kyu', 'brown')")
    if db.session.query(Grade.id).filter_by(name='1.dan').scalar() is None:
        db.engine.execute("INSERT INTO grade (name, color) "
                + "VALUES('1.dan', 'black')")
except:
    pass