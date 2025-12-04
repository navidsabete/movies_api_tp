import oracledb

_un = ""
_cs = ""
_pw = ''
_connection = None


def db():
    global _pw, _connection

    if _connection:
        return _connection

    _connection = oracledb.connect(user=_un, password=_pw, dsn=_cs)
    return _connection


