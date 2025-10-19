# ベースイメージ
FROM python:3.11-slim

# 環境変数
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリ
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# Flaskのポート
EXPOSE 5000

# DB初期化（初回のみ自動実行したい場合）
# RUN flask db upgrade

# 起動コマンド（Renderと同じ）
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]