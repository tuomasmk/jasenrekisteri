from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields import HiddenField, IntegerField
from wtforms.fields.html5 import DateField
from application.groups.models import Group
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput
import datetime
import wtforms_sqlalchemy.fields as f                                                                                                                                                                                                                                                                    
def get_pk_from_identity(obj):
    cls, key = f.identity_key(instance=obj)[:2]
    return ':'.join(f.text_type(x) for x in key)                             
f.get_pk_from_identity = get_pk_from_identity

def getGroups():
	return Group.query

class MemberForm(FlaskForm):
	firstnames = StringField("First names", [validators.Length(min=2)])
	lastname = StringField("Last name", [validators.Length(min=2)])
	grouplist = QuerySelectField("Group", query_factory=getGroups, get_label="name", get_pk=lambda g: g.id)

	class Meta:
		csrf = False

class MemberGroupForm(FlaskForm):
	groups = QuerySelectField(query_factory=getGroups, allow_blank=False)

	class Meta:
		csrf = False

class MemberPracticeForm(FlaskForm):
	date = DateField('Date', default=datetime.datetime.now().date())
	member_id = HiddenField('Id', validators=[DataRequired()])

	class Meta:
		csrf = False