from flask import Blueprint, render_template, request, redirect, url_for, flash
from .database import db
from .models import User

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@bp.route("/add", methods=["GET", "POST"])
def add():
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
            user = User(name=name, age=age)
            db.session.add(user)
            db.session.commit()
            flash("ユーザーを追加しました", "success")
            return redirect(url_for("main.index"))

    return render_template("form.html", errors=errors, user=None)


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