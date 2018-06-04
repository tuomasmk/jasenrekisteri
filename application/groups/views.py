from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.groups.models import Group
from application.groups.forms import GroupForm

@app.route("/groups/", methods=["GET"])
@login_required
def groups_index():
	return render_template("groups/list.html", groups = Group.query.all())

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
