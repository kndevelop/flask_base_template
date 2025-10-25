# Flask Base Template 🧱

Flask + SQLite/PostgreSQL + Docker + Render + GitHub Actions  
開発からデプロイまで自動化された、実践的なWebアプリケーションテンプレートです。

---

## 🚀 Features

- Flask + SQLAlchemy + Flask-Migrate による堅牢な構成  
- SQLite（ローカル）／PostgreSQL（Render本番）両対応  
- Bootstrap 5 + flashメッセージで見やすいUI  
- ページネーション・404/500ページ対応済み  
- pytest による自動テスト  
- GitHub Actionsでの自動CI/CD  
- Renderで本番・ステージング環境を分離運用可能  

---

## 🧱 使用技術スタック

| カテゴリ | 使用技術 |
|-----------|-----------|
| 言語 | Python 3.11 |
| Webフレームワーク | Flask |
| テンプレート | Jinja2 |
| ORM / DB | SQLAlchemy + SQLite/PostgreSQL |
| マイグレーション | Flask-Migrate |
| スタイル/UI | Bootstrap 5 |
| テスト | pytest + BeautifulSoup |
| CI/CD | GitHub Actions |
| ホスティング | Render |

---

## 📂 ディレクトリ構成

```
flask-base-template/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── database.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── form.html
│ │ ├── edit.html
│ │ ├── 404.html
│ │ └── 500.html
│ └── static/
├── instance/
│ └── app.db
├── tests/
│ └── test_app.py
├── .github/workflows/
│ ├── deploy.yml
│ ├── deploy_staging.yml
│ └── deploy_production.yml
├── config.py
├── docker-compose.yml
├── Dockerfile
├── .env
├── requirements.txt
├── run.py
└── README.md

```
---

## ⚙️ ローカル開発（Docker使用）

```bash
# 初回ビルド・起動
docker compose up --build

# DBリセットしたい場合
rm -f instance/app.db
docker compose up --build

```

アプリは http://127.0.0.1:5000 で起動します。


## 🧪 テスト実行
docker compose run --rm test pytest -v


## 🧪 GitHub Actions（CI/CD）

本テンプレートには GitHub Actions が含まれており、
以下のように動作します：


| イベント         | 実行内容                      |
| --------------- | ------------------------------|
| push to develop | ステージング環境へ自動デプロイ   |
| push to main    | 本番環境へ自動デプロイ          |
| pull_request    | pytestのみ実行（デプロイなし）  |

## ☁️ Render へのデプロイ手順
① 新しい Web Service を作成

Render ダッシュボードで “New → Web Service” を選択

GitHub からこのリポジトリを選択

設定を以下のように指定
```
設定項目	    値
Name	flask-base-template
Environment	Python
Build Command	pip install -r requirements.txt
Start Command	gunicorn run:app
Root Directory	（リポジトリ直下、または python_sample/flask-sqlite-sample など）
Auto Deploy	ON
Region	Singapore or Oregon（どちらでも可）
```

② 環境変数（Render Dashboard → Environment）
Key	Value	備考
SECRET_KEY	任意のランダム文字列	Flaskのセッション保護用
FLASK_ENV	production	開発時は development
DATABASE_URL	（省略可：SQLite使用時は不要）	
③ デプロイ完了後

Renderが自動でアプリをビルド・起動します。

URL例: https://flask-base-template.onrender.com

| 環境         | ブランチ    | サービスID                | デプロイ先                                                                                                |
| ---------- | ------- | --------------------- | ---------------------------------------------------------------------------------------------------- |
| Staging    | develop | （例）`srv-xxxx-staging` | [https://flask-base-template-staging.onrender.com](https://flask-base-template-staging.onrender.com) |
| Production | main    | （例）`srv-xxxx-prod`    | [https://flask-base-template.onrender.com](https://flask-base-template.onrender.com)                 |


## 🧩 今後の拡張例

Flask-Loginで認証機能を追加

PostgreSQLに移行（Renderで無料枠あり）

REST APIエンドポイントを追加

ReactやVueと統合してフロントエンド強化

## 📄 ライセンス

MIT License
自由に改変・利用可能です。
