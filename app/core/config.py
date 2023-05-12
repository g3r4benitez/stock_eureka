import os
import psycopg2

from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, ".env"))
APP_VERSION = "0.0.1"
APP_NAME = "APP_name"
API_PREFIX = "/api"

# Env vars
IS_DEBUG: bool = _config("IS_DEBUG", cast=bool, default=False)

DB_URL: str = _config("DB_URL", cast=str)

ALPHA_URL: str = _config("ALPHA_URL", cast=str)
ALPHA_APIKEY: str = _config("ALPHA_APIKEY", cast=str)
SIMBOLS = ("META", "AAPL", "MSFT", "GOOGL", "AMZN")

REQUEST_PERSECOND = _config("REQUEST_PERSECOND", cast=int, default=1)
REQUEST_PERMINUTE = _config("REQUEST_PERMINUTE", cast=int, default=5)
ONE_SECOND = 1
ONE_MINUTE = 60

def get_connection():

    host = _config("DB_HOST", cast=str, default="")
    port = _config("DB_PORT", cast=str, default="")
    database = _config("DB_NAME", cast=str, default="")
    user = _config("DB_USERNAME", cast=str, default="")
    password = _config("DB_PASSWORD", cast=str, default="")

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    return conn
