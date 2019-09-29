import pymysql

#mysql connection
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "re^mp123"
DB_DBASE = "spe_development"


def mysql_execute_query(query):
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        db=DB_DBASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit = True)
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data


def mysql_insert_query(query):
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        db=DB_DBASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True)
    cursor = db.cursor()
    cursor.execute(query)

def mysql_insert_bulk_query(query):
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        db=DB_DBASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True)
    cursor = db.cursor()
    for statement in query.split(';'):
        if len(statement) > 1:
            cursor.execute(statement + ';')