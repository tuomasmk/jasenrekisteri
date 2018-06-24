from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField, BooleanField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    redirectUrl = HiddenField("redirectUrl")
  
    class Meta:
        csrf = False

class CreateUserForm(FlaskForm):
    name = HiddenField("Name")
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=4)])
    admin = BooleanField("Admin")
    member = HiddenField("Member")

    class Meta:
        csrf = False

class ModifyUserForm(FlaskForm):
    name = HiddenField("Name")
    username = StringField("Username", [validators.Length(min=4)])
    admin = BooleanField("Admin")
    member = HiddenField("Member")

    class Meta:
        csrf = False

class ResetPasswordForm(FlaskForm):
    password = PasswordField("New password", [validators.Length(min=2)])

    class Meta:
        csrf = False