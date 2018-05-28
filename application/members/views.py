from application import app, db
from flask import render_template, request, redirect, url_for
from application.members.models import Member

@app.route("/members/", methods=["GET"])
def members_index():
	return render_template("members/list.html", members = Member.query.all())
@app.route("/members/new/")
def members_form():
    return render_template("members/new.html")

@app.route("/members/", methods=["POST"])
def members_create():
	m = Member(request.form.get("name"))

	db.session().add(m)
	db.session().commit()

	return redirect(url_for("members_index"))
