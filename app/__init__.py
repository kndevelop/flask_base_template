from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # --- エラーハンドラ登録 ---
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template("500.html"), 500

    db.init_app(app)
    Migrate(app, db)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # テストや初回起動用：DBテーブルを作成
    with app.app_context():
        db.create_all()

    return app