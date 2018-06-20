from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        next = request.args.get("next")
        print(next)
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
    print(next)
    print("Next if")
    if next != None:
        print("Not None")
        if next != '':
            print("Not empty")
            return redirect(next)
    return redirect(url_for("index"))
    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))