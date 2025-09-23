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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username, password_hash FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user