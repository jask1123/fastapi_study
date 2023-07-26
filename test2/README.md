# FastAPI practice
fastAPIをMySQLと接続してDockerで構築

## Set up
Dockerでbuild
```bash
Docker-compose build
```
Dockerを起動（-dでバックで起動）
```bash
Docker-compose up -d
```

# Swagger UI
localhost:8080/docs

# MySQLとの接続を確認
```bash
docker-compose exec db mysql fastapi-practice-db
```

# 初回docker起動方法
```bash
mkdir .dockervenv
```

# poetryによるpython環境セットアップ
```bash
docker-compose run --entrypoint "poetry init --name demo-app --dependency fastapi --dependency uvicorn[standard]" demo-app
```

Authorのパートのみnの入力を求められるので、適当に入力してEnterを押す
# fastapiのpoetryの定義ファイル作成
```bash
docker compose run --entrypoint "poetry install --no-root" demo-app
docker compose build --no-cache
docker compose exec demo-app poetry add sqlalchemy pymysql
```
#apiモジュールのmigrate_dbScriptを実行する
```bash
docker compose exec demo-app poetry run python  -m api.migrate_db.py
```
#何故かホストに接続的ないことがあるので、その時は以下のコマンドを実行する
dbコンテナに接続
コンテナ内でコマンドを実行
```bash
musql
CREATE USER 'sample_user' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'sample_user'@'%' WITH GRANT OPTION;
create database demo;
```
そしたらapiモジュールのmigrate_dbScriptを実行するが実行できる。

非同期処理を行うためにaiomysqlをインストールする
```bash
docker compose exec demo-app poetry add aiomysql
```

# user情報登録のためにbcryptをインストールする
pyproject.tomlに以下を追加
```bash
[tool.poetry.dependencies]
python = "^3.10"
fastapi = "^0.99.1"
uvicorn = {extras = ["standard"], version = "^0.22.0"}
sqlalchemy = "^2.0.17"
pymysql = "^1.1.0"
aiomysql = "^0.2.0"
python-jose = {extras = ["cryptography"], version = "^3.0"}
passlib = {extras = ["bcrypt"], version = "^1.0"}
python-multipart = "^0.0.5"
```
```bash
poetry update
```
をコンテナ内で実行する

#詰まったところ
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
このエラーが出たときは、以下のコマンドを実行する
```bash
mysql -h 127.0.0.1 -P 3306 -u root -proot
```
