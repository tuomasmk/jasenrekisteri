from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.members.models import Member
from application.members.forms import MemberForm, MemberGroupForm, MemberPracticeForm
from application.practice.models import Practice
from datetime import date

@app.route("/members/", methods=["GET"])
@login_required
def members_index():
	return render_template("members/list.html", 
		members = Member.query.all(), 
		members_w_group=Member.find_members_with_group())

@app.route("/members/new/")
@login_required
def members_form():
    return render_template("members/new.html", 
		form = MemberForm())

@app.route("/members/", methods=["POST"])
@login_required
def members_create():
	form = MemberForm(request.form)

	if not form.validate():
		return render_template("members/new.html", form = form)

	m = Member(form.firstnames.data, form.lastname.data, 
		form.grouplist.data.getId())

	db.session().add(m)
	db.session().commit()

	return redirect(url_for("members_index"))

@app.route("/members/form", methods=["GET", "POST"])
def members_group():
	form = MemberGroupForm()
	return render_template('members/form.html', form=form)

@app.route("/members/<id>", methods=["GET"])
def members_practices(id):
	form = MemberPracticeForm()
	form.member_id.data = id

	return render_template('members/practices.html', 
		practices = Member.find_member_and_practices(id), form=form)

@app.route("/members/practices", methods=["POST"])
def member_practices_create():
	form = MemberPracticeForm(request.form)

	if not form.validate():
		return render_template("members/practices.html", 
			form=form)

	p = Practice(form.date.data, form.member_id.data)

	db.session().add(p)
	db.session().commit()
	return redirect(url_for("members_index"))