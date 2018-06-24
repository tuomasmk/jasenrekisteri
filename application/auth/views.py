from flask import flash, render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User, Role
from application.auth.forms import LoginForm, CreateUserForm, ResetPasswordForm, ModifyUserForm
from application.members.models import Member

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        next = request.args.get("next")
        form = LoginForm()
        form.redirectUrl.data = next
        return render_template("auth/loginform.html", form = form)

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)

    next = form.redirectUrl.data
    if next != None:
        if next != '':
            return redirect(next)
    return redirect(url_for("index"))
    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/user/<int:id>", methods=["GET", "POST"])
@login_required(role="ANY")
def create_user(id):
    member = Member.query.filter_by(id=id).first()
    if member is None:
        flash("No such member", "error")
        return redirect(url_for("members_index"))
    current_user = User.query.filter_by(id=session["user_id"]).first()
    if (current_user.member_id is None or current_user.member_id != member.id) and not "ADMIN" in current_user.roles():
        flash("You are not authorized to use this resource, please contact system administrator", "error")
        return redirect(request.referrer or '/')
    if request.method == "GET":
        user = User.query.filter_by(member_id=id).first()
        form = CreateUserForm
        form = CreateUserForm(obj=user)
        if form.name.data is None or form.name.data == '':
            form.name.data = member.firstnames
        return render_template("auth/createuser.html",
                form = form,
                id = id)
    if request.method == "POST":
        form = CreateUserForm(request.form)

        if not form.validate():
            return render_template("auth/createuser.html", 
            form = form,
            id = id)

        if not db.session.query(User.id).filter_by(username=form.username.data).scalar() is None:
            flash("User with the same username already exists", "error")
            return render_template("auth/createuser.html",
                form = form,
                id = id)
        if not db.session.query(User.id).filter_by(member_id=id).scalar() is None:
            # should never get here
            flash("User for this member already exists", "error")
            return redirect(url_for("member_details", id=id))
        user = User(form.name.data, form.username.data, form.password.data)
        form.member.data = member
        form.populate_obj(user)
        db.session().add(user)
        db.session.commit()
        if "admin" in request.form:
            add_admin(user)
        flash("User created", "success")
        return redirect(url_for("members_index"))

@app.route("/user/modify/<int:id>", methods=["GET", "POST"])
@login_required(role="ANY")
def modify_user(id):
    user = User.query.filter_by(member_id=id).first()
    if user is None:
        flash("No such user", "error")
        return redirect(url_for("member_details", id=id))
    current_user = User.query.filter_by(id=session["user_id"]).first()
    if not "ADMIN" in current_user.roles() and current_user.id != user.id:
        flash("You are not authorized to use this resource, please contact system administrator", "error")
        return redirect(request.referrer or '/')
    if request.method == "GET":
        form = ModifyUserForm(obj=user)
        form.admin.data = "ADMIN" in user.roles()
        return render_template("auth/modifyuser.html", 
            id = id,
            form = form)
    else:
        print("\n post request")
        form = ModifyUserForm(request.form)
        if not form.validate():
            return render_template("auth/modifyuser.html",
            form = form,
            id = id)
        if "admin" in request.form:
            add_admin(user)
        else:
            delete_admin(user.id)
        member = Member.query.filter_by(id=id).first()
        form.member.data = member
        form.populate_obj(user)
        db.session.commit()
        flash("User updated", "success")
        return redirect(url_for("members_index"))

@app.route("/user/changepw/<int:id>", methods=["GET", "POST"])
@login_required(role="ANY")
def reset_password(id):
    user = User.query.filter_by(member_id=id).first()
    if user is None:
        flash("No such user", "error")
        return redirect(url_for("member_details", id=id))
    current_user = User.query.filter_by(id=session["user_id"]).first()
    if not "ADMIN" in current_user.roles() and current_user.id != user.id:
        flash("You are not authorized to use this resource, please contact system administrator", "error")
        return redirect(request.referrer or '/')
    if request.method == "GET":
        form = ResetPasswordForm()
        return render_template("auth/resetpw.html", 
            id = id,
            form = form)
    else:
        form = ResetPasswordForm(request.form)
        if not form.validate():
            return render_template("auth/resetpw.html",
            form = form,
            id = id)
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash("Password changed", "success")
        return redirect(url_for("members_index"))

def delete_admin(id):
    role = Role.query.filter_by(user_id=id, name="ADMIN").first()
    if role != None:
        db.session.delete(role)
    


def add_admin(user):
    if db.session.query(Role.id).filter_by(user_id=user.id, name="ADMIN").scalar() is None:
        role = Role()
        role.name="ADMIN"
        role.user_id=user.id
        db.session().add(role)
        db.session.commit()