import pytest
from app import create_app
from app.database import db

@pytest.fixture
def client():
    # メモリ上DBを使う
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()  # ここでテーブルを作る

    return app.test_client()

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200