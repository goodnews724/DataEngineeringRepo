import dotenv
import os

# .env 파일 경로 찾기(자동으로 찾아줌)
env_path = dotenv.find_dotenv()

# .env 파일  (내용이 있으면 -> True, 없으면 -> False)
dotenv.load_dotenv(env_path)

# 1) connection 생성
DB_SETTINGS = dict(
    mysql_params = dict(
        engine_name = os.getenv('MYSQL_ENGINE_NAME', ""),
        user = os.getenv('MYSQL_USER', ""),
        password = os.getenv('MYSQL_PASSWORD', ""),
        host = os.getenv('MYSQL_HOST', ""),
        port = os.getenv('MYSQL_PORT', ""),
        database = os.getenv('MYSQL_DATABASE', "")
    ),

    pg_params = dict(
        engine_name = os.getenv('PG_ENGINE_NAME', ""),
        user = os.getenv('PG_USER', ""),
        password = os.getenv('PG_PASSWORD', ""),
        host = os.getenv('PG_HOST', ""),
        port = os.getenv('PG_PORT', ""),
        database = os.getenv('PG_DATABASE', "")
    )
)

DB_SETTINGS
