import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    # MariaDB
    MARIADB_HOST = os.getenv("MARIADB_HOST")
    MARIADB_PORT = int(os.getenv("MARIADB_PORT"))
    MARIADB_USER = os.getenv("MARIADB_USER")
    MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")
    MARIADB_DB = os.getenv("MARIADB_DB")