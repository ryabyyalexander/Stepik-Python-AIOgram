import sqlite3

async def add_users(d1, d2, d3, d4):
    with sqlite3.connect('m158.db') as db:
        cursor = db.cursor()
        #cursor.execute("DROP TABLE IF EXISTS user")
        cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            chat INTEGER,
            name VARCHAR,
            last_name VARCHAR,
            username VARCHAR)""")
        cursor.execute("""INSERT INTO user VALUES(?, ?, ?, ?)""", (d1, d2, d3, d4))



async def get_user(x):
    with sqlite3.connect('m158.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT {x} FROM user ORDER BY ROWID DESC")
        x = cursor.fetchone()
        return x[0]

async def create_session(user):
    with sqlite3.connect(f'user'+'.db') as db:
        cursor = db.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {user}")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {user} (chat INTEGER)""")
        cursor.execute(f"""INSERT INTO {user} VALUES(?)""", (int(user[1:]),))
