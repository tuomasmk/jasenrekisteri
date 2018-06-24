from application import app, db, login_required
from flask import flash, render_template, request, redirect, url_for, session
from application.members.models import Grade, Member
from application.members.forms import MemberForm, MemberGroupForm, MemberPracticeForm, SimpleMemberForm
from application.groups.models import Group
from application.practice.models import Practice
from application.auth.models import User
from datetime import date, timedelta

@app.route("/members/", methods=["GET"])
@login_required(role="ANY")
def members_index():
	return render_template("members/list.html", 
		members_w_group=Member.find_members_with_group())

@app.route("/members/new/")
@login_required(role="ANY")
def members_form():
    return render_template("members/new.html", 
		form = MemberForm())

@app.route("/members/", methods=["POST"])
@login_required(role="ANY")
def members_create():
	form = MemberForm(request.form)

	if not form.validate():
		return render_template("members/new.html", form = form)

	member = Member(firstnames=form.firstnames.data, 
		lastname=form.lastname.data, group_id=form.group.data.getId())
	form.populate_obj(member)
	db.session().add(member)
	db.session.commit()
	return redirect(url_for("members_index"))

#@app.route("/members/form", methods=["GET", "POST"])	
#def members_group():
	#form = MemberGroupForm()
	#return render_template('members/form.html', form=form)

@app.route("/members/<int:id>", methods=["GET"])
def members_practices(id):
	form = MemberPracticeForm()
	form.member_id.data = id
	
	return render_template('members/practices.html', 
		practices = Member.find_practices_for_member(id), 
		practiceCount = Member.find_member_and_practices(id), 
		deleteLimit = date.today() - timedelta(30),
		form=form)

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

@app.route("/members/delete/<int:id>", methods=["POST"])
@login_required(role="ANY")
def members_delete(id):
	member = Member.query.filter_by(id=id).first()
	if member is None:
		flash("No such member", "error")
		return redirect(url_for("members_index"))
	user = User.query.filter_by(id=session["user_id"]).first()
	if (user.member_id is None or user.member_id != member.id) and not "ADMIN" in user.roles():
		flash("You are not authorized to use this resource, please contact system administrator", "error")
		return redirect(request.referrer or '/')
	db.session().delete(member)
	db.session().commit()

	return redirect(url_for("members_index"))

@app.route("/members/<int:id>/details", methods=["GET", "POST"])
@login_required(role="ANY")
def member_details(id):
	member = Member.query.filter_by(id=id).first()
	if member is None:
		flash("No such member", "error")
		return redirect(url_for("members_index"))
	user = User.query.filter_by(id=session["user_id"]).first()
	if (user.member_id is None or user.member_id != member.id) and not "ADMIN" in user.roles():
		flash("You are not authorized to use this resource, please contact system administrator", "error")
		return redirect(request.referrer or '/')
	if request.method == "GET":
		user = User.query.filter_by(member_id=member.id).first()
		form = MemberForm()
		form = MemberForm(obj=member)
		return render_template("members/details.html",
		details = form,
		id = id,
		user = user)
	else:
		form = MemberForm(request.form)
		form.populate_obj(member)
		db.session.commit()
		flash("Member details updated", "success")
		return redirect(url_for("members_index"))