from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    Migrate(app, db)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # テストや初回起動用：DBテーブルを作成
    with app.app_context():
        db.create_all()

    return app