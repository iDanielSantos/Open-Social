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