import sqlite3


def save_all_img(d):
    with sqlite3.connect('save.db') as db:
        cursor = db.cursor()
        # cursor.execute("""DROP TABLE IF EXISTS img""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS img(id TEXT)""")
        cursor.execute("""INSERT INTO img VALUES(?)""", (d,))


def get_img():
    with sqlite3.connect('save.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM img ORDER BY rowid DESC")
        return cursor.fetchone()[0]


def save_desc(t):
    with sqlite3.connect('save.db') as db:
        cursor = db.cursor()
        # cursor.execute("""DROP TABLE IF EXISTS desc""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS desc(dsc TEXT)""")
        cursor.execute("""INSERT INTO desc VALUES(?)""", (t,))


def get_desc():
    with sqlite3.connect('save.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT dsc FROM desc ORDER BY rowid DESC")
        return cursor.fetchone()[0]
