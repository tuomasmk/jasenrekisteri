from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    redirectUrl = HiddenField("redirectUrl")
  
    class Meta:
        csrf = False