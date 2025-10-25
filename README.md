# Flask Base Template

Flask + SQLite + Render + GitHub Actions で構築した  
シンプルで運用しやすい Web アプリケーションテンプレートです。  
CRUD 機能付きの Flask アプリを、無料の Render 環境に自動デプロイできます。

---

## 🚀 Features

- Flask + SQLite の軽量構成  
- Bootstrap によるシンプルなUI  
- GitHub Actions による自動テスト・デプロイ  
- Render 無料プランで動作確認済み  
- 開発（staging）と本番（production）環境をブランチで分離可能  

---

## 🧱 使用技術 / フレームワーク / ライブラリ

| カテゴリ | 使用技術 |
|-----------|-----------|
| 言語 | Python 3.11 |
| Webフレームワーク | Flask |
| テンプレート | Jinja2 |
| ORM / DB | SQLAlchemy + SQLite |
| マイグレーション | Flask-Migrate |
| スタイル | Bootstrap 5 |
| テスト | pytest |
| CI/CD | GitHub Actions |
| ホスティング | Render |

---

## 💡 ディレクトリ構成（例）

```
flask-base-template/
├── app/
│ ├── __init__.py
│ ├── routes.py
│ ├── models.py
│ ├── templates/
│ └── static/
├── tests/
│ └── test_app.py
├── requirements.txt
├── config.py
├── run.py
└── README.md

```
---

## ⚙️ ローカル開発環境のセットアップ

```bash
# 仮想環境の作成
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 依存関係のインストール
pip install -r requirements.txt

# 初期DB作成
flask db upgrade

# 実行
flask run

```

アプリは http://127.0.0.1:5000 で起動します。

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

## 🧪 GitHub Actions（CI/CD）

本テンプレートには GitHub Actions が含まれており、
以下のように動作します：

イベント	動作内容
push to develop	ステージング環境に自動デプロイ
push to main	本番環境に自動デプロイ
pull_request	pytestでテストを実行（デプロイは行わない）

💬 pytest が失敗した場合は Render へのデプロイはスキップされます。

## 🧩 今後の拡張例

Flask-Loginで認証機能を追加

PostgreSQLに移行（Renderで無料枠あり）

REST APIエンドポイントを追加

ReactやVueと統合してフロントエンド強化

## 📄 ライセンス

MIT License
自由に改変・利用可能です。

## ✨ デモ

Production: https://flask-base-template.onrender.com

Staging: https://flask-base-template-staging.onrender.com