from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.members.models import Member
from application.members.forms import MemberForm
from application.members.forms import MemberGroupForm

@app.route("/members/", methods=["GET"])
@login_required
def members_index():
	return render_template("members/list.html", members = Member.query.all())

@app.route("/members/new/")
@login_required
def members_form():
    return render_template("members/new.html", form = MemberForm())

@app.route("/members/", methods=["POST"])
@login_required
def members_create():
	form = MemberForm(request.form)

	if not form.validate():
		return render_template("members/new.html", form = form)

	m = Member(form.firstnames.data, form.lastname.data, form.grouplist.data.getId())

	db.session().add(m)
	db.session().commit()

	return redirect(url_for("members_index"))

@app.route("/members/form", methods=["GET", "POST"])
def members_group():
	form = MemberGroupForm()
	return render_template('members/form.html', form=form)
