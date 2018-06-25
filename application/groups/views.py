from flask import flash, render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.practice.models import Practice
from datetime import datetime

@app.route("/groups/", methods=["GET"])
@login_required(role="ANY")
def groups_index():
	return render_template("groups/list.html", 
        groups = Group.find_group_member_count(),
        emptyGroups = Group.empty_group_count())

@app.route("/groups/new/")
@login_required(role="ANY")
def groups_form():
    return render_template("groups/new.html", form = GroupForm())

@app.route("/groups/", methods=["POST"])
@login_required(role="ADMIN")
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)

    g = Group(form.name.data)

    db.session().add(g)
    db.session().commit()

    flash('Group added succesfully', 'success')
    return redirect(url_for("groups_index"))

@app.route("/groups/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def groups_practices(id):
    if request.method == "POST":
        form = request.form
        for key in form:
            if key != "date":
                p = Practice(datetime.strptime(form["date"], "%Y-%m-%d"), int(key))
                db.session().add(p)
        db.session().commit()
        flash("Participations added", "success")
    return render_template("groups/practices.html", 
        members = Group.find_group_members(id),
        now = datetime.now().date())
    
@app.route("/groups/delete/<int:id>", methods=["POST"])
@login_required(role="ADMIN")
def groups_delete(id):
    g = Group.query.filter_by(id=id).first()
    if not g is None:
        db.session().delete(g)
        db.session().commit()
    
    return redirect(url_for("groups_index"))

@app.route("/groups/details/<int:id>", methods=["GET"])
@login_required(role="ANY")
def groups_details(id):
    group = Group.query.filter_by(id=id).first()
    return render_template("groups/details.html", 
        group = group,
        coaches = Group.group_coaches(id),
        members = len(group.members),
        practices = Group.practices_per_group(id))