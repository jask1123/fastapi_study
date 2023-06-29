# fastAPI practice
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
docker compose exec demo-app poerty run python  -m api.migrate_db.py
```