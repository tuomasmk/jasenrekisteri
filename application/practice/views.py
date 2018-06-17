from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.practice.models import Practice

@app.route("/practices/delete/<id>", methods=["POST"])
def delete_practice(id):
    form = request.form
    print("Form")
    print(form)
    print(form["member_id"])
    print(url_for("members_index", id=request.form["member_id"]))
    p = Practice.query.filter_by(id=id).first()
    print(p.id)
    print(p.date)
    if not p is None:
        db.session().delete(p)
        db.session().commit()

    return redirect(url_for("members_practices", id=request.form["member_id"]))