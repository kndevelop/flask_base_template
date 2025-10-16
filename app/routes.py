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
    if request.method == "POST":
        name = request.form["name"]
        age = request.form.get("age", type=int)
        user = User(name=name, age=age)
        db.session.add(user)
        db.session.commit()
        flash("ユーザーを追加しました！", "success")
        return redirect(url_for("main.index"))
    return render_template("form.html")

@bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.name = request.form["name"]
        user.age = request.form.get("age", type=int)
        db.session.commit()
        flash("更新しました！", "info")
        return redirect(url_for("main.index"))
    return render_template("edit.html", user=user)

@bp.route("/delete/<int:user_id>", methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("削除しました。", "danger")
    return redirect(url_for("main.index"))