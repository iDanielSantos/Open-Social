from flask_bcrypt import Bcrypt
import mariadb
from config import Config

bcrypt = Bcrypt()

def get_db_connection():
    return mariadb.connect(
        host=Config.MARIADB_HOST,
        port=Config.MARIADB_PORT,
        user=Config.MARIADB_USER,
        password=Config.MARIADB_PASSWORD,
        database=Config.MARIADB_DB
    )

def get_user_by_username(username):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT username, password_hash FROM users WHERE username = ?", (username,))
            return cur.fetchone()

def add_user_to_db(username, display_name, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8') 
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (username, display_name, password_hash) VALUES (?, ?, ?)", (username, display_name, password_hash))

def check_password(password_hash, password):
    return bcrypt.check_password_hash(password_hash, password)
