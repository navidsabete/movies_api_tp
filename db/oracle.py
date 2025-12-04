from db import db_secret
import oracledb


def db():
    global _pw, _connection

    if db_secret._connection:
        return db_secret._connection

    db_secret._connection = oracledb.connect(user=db_secret._un, password=db_secret._pw, dsn=db_secret._cs)
    return db_secret._connection