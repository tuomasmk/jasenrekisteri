from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.practice.models import Practice
from datetime import datetime

@app.route("/groups/", methods=["GET"])
@login_required
def groups_index():
	return render_template("groups/list.html", groups = Group.find_group_member_count())

@app.route("/groups/new/")
@login_required
def groups_form():
    return render_template("groups/new.html", form = GroupForm())

@app.route("/groups/", methods=["POST"])
@login_required
def groups_create():
	form = GroupForm(request.form)

	if not form.validate():
		return render_template("groups/new.html", form = form)

	g = Group(form.name.data)

	db.session().add(g)
	db.session().commit()

	return redirect(url_for("groups_index"))

@app.route("/groups/<id>", methods=["GET", "POST"])
def groups_details(id):

    if request.method == "POST":
        form = request.form
        for key in form:
            if key != "date":
                p = Practice(datetime.strptime(form["date"], "%Y-%m-%d"), int(key))
                db.session().add(p)
        db.session().commit()
    return render_template("groups/details.html", 
        members = Group.find_group_members(id),
        now = datetime.now().date())
    