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

    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, "danger")

    return render_template("add.html", form=form)


@bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    errors = {}
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", type=int)

        # バリデーション
        if not name:
            errors["name"] = ["名前は必須です"]
        if age is None or age < 0:
            errors["age"] = ["年齢は0以上で入力してください"]

        if not errors:
            user.name = name
            user.age = age
            db.session.commit()
            flash("更新しました", "info")
            return redirect(url_for("main.index"))

    return render_template("form.html", errors=errors, user=user)


@bp.route("/delete/<int:user_id>", methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("削除しました", "danger")
    return redirect(url_for("main.index"))