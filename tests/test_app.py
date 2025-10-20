import pytest
from bs4 import BeautifulSoup
from app import create_app
from app.database import db
from app.models import User

# ─── ヘルパー ───────────────────────────────
def get_text_from_response(response):
    """HTMLのbytesをテキスト化してタグを除去"""
    soup = BeautifulSoup(response.data, "html.parser")
    return soup.get_text()


# ─── pytest fixture ─────────────────────────
@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # 毎回クリーンなDB
        "WTF_CSRF_ENABLED": False,                        # CSRFをテスト中は無効化
    })

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


# ─── テスト本体 ────────────────────────────
def test_index_page(client):
    """トップページが表示できるか"""
    response = client.get("/")
    assert response.status_code == 200
    text = get_text_from_response(response)
    assert "ユーザー" in text


def test_add_user_success(client):
    """ユーザー追加（正常系）"""
    response = client.post(
        "/add",
        data={"name": "田中太郎", "age": 28},
        follow_redirects=True,
    )
    text = get_text_from_response(response)
    assert response.status_code == 200
    assert "ユーザーを追加しました" in text
    assert User.query.count() == 1


def test_add_user_validation_error(client):
    """ユーザー追加（バリデーションエラー）"""
    response = client.post(
        "/add",
        data={"name": "", "age": -5},  # 無効な入力
        follow_redirects=True,
    )
    text = get_text_from_response(response)
    assert response.status_code == 200
    # 名前や年齢のエラーメッセージが表示されているか確認
    assert "名前は必須です" in text or "年齢は0以上で入力してください" in text
    assert User.query.count() == 0


def test_edit_user(client):
    """ユーザー編集"""
    user = User(name="太郎", age=20)
    db.session.add(user)
    db.session.commit()

    response = client.post(
        f"/edit/{user.id}",
        data={"name": "次郎", "age": 30},
        follow_redirects=True,
    )
    text = get_text_from_response(response)
    assert response.status_code == 200
    updated = User.query.get(user.id)
    assert updated.name == "次郎"
    assert updated.age == 30


def test_delete_user(client):
    """ユーザー削除"""
    user = User(name="削除対象", age=40)
    db.session.add(user)
    db.session.commit()

    response = client.post(f"/delete/{user.id}", follow_redirects=True)
    text = get_text_from_response(response)
    assert response.status_code == 200
    assert User.query.count() == 0