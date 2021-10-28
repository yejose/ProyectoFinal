import sqlite3
from sqlite3.dbapi2 import Error

def conectar():
    dbname = "Plataforma.db"
    conn = sqlite3.connect(dbname)
    return conn