from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User
from app.forms import UserForm
from .database import db
from .models import User

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        user = User(name=name, age=age)
        db.session.add(user)
        db.session.commit()
        flash("ユーザーを追加しました", "success")
        return redirect(url_for("main.index"))

    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "danger")

    users = User.query.all()
    return render_template("index.html", users=users)

@bp.route("/add", methods=["GET", "POST"])
def add():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, age=form.age.data)
        db.session.add(user)
        db.session.commit()
        flash("ユーザーを追加しました", "success")
        return redirect(url_for("main.index"))
    return render_template("form.html", form=form)


@bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.age = form.age.data
        db.session.commit()
        flash("更新しました", "info")
        return redirect(url_for("main.index"))
    return render_template("edit.html", form=form, user=user)


@bp.route("/delete/<int:user_id>", methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("削除しました", "danger")
    return redirect(url_for("main.index"))