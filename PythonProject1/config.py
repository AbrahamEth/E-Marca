# config.py
import os

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "127.0.0.1"),
    "port": int(os.environ.get("DB_PORT", 3306)),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASS", ""),
    "db": os.environ.get("DB_NAME", "ecommerce_demo"),
    "charset": "utf8mb4",
    "cursorclass": None
}
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
