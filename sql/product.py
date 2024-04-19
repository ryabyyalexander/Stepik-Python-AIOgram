import sqlite3


def create_product(d):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        # cursor.execute("DROP TABLE IF EXISTS product")
        cursor.execute("""CREATE TABLE IF NOT EXISTS product(
            pos_pic VARCHAR,
            description TEXT,
            voice VARCHAR,
            video VARCHAR,
            category VARCHAR,
            sub_category VARCHAR,
            brand VARCHAR,
            article_no VARCHAR,
            color VARCHAR,
            size VARCHAR,
            price INTEGER,
            Tamila INT)""")
        cursor.execute("INSERT INTO product(pos_pic, description, category, sub_category, brand, size) \
        VALUES( ?, ?, ?, ?, ?, ?)", d)


def get_new():
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product WHERE description LIKE '%NEW%' ORDER BY category, brand DESC")
        product = cursor.fetchall()
        return product


def get_product(arg1, n1, arg2, n2):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE {arg1} = {n1} and {arg2} = {n2}")
        product = cursor.fetchall()
        return product


def find_size_db(d):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(
            f"""SELECT * FROM product WHERE (size LIKE '%{d}%' or size LIKE '{d}%' or size LIKE '%{d}') and seasons = 0
            ORDER BY category, brand DESC, sub_category DESC""")
        product = cursor.fetchall()
        return product


def find_prod_db(d, *args):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        if len(args) > 0:
            cursor.execute(f"""SELECT * FROM product
            WHERE (category = '{d}' or sub_category = '{d}')
            and (size LIKE '%{args[0]}%' or size LIKE '{args[0]}%'
            or size LIKE '%{args[0]}'
            or size LIKE '%{args[0]}%' or size LIKE '{args[0]}%' or size LIKE '%{args[0]}')
            ORDER BY seasons, category, brand DESC""")
            product = cursor.fetchall()
            return product
        else:
            cursor.execute(f"""SELECT * FROM product
                        WHERE category = '{d}' or sub_category = '{d}' """)
            product = cursor.fetchall()
            return product


# REPORT
def get_product_brand(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE Tamila = 1 and brand = '{p}'")
        product = cursor.fetchall()
        return product


def get_product_category(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE Tamila = 1 and category = '{p}'")
        product = cursor.fetchall()
        return product


def get_product_sub_category(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(
            f"SELECT * FROM product WHERE Tamila = 1 and category = 'т р и к о т а ж' and sub_category = '{p}'")
        product = cursor.fetchall()
        return product


def get_product_brand158(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE Tamila = 0 and brand = '{p}'")
        product = cursor.fetchall()
        return product


def get_product_category158(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE Tamila = 0 and category = '{p}'")
        product = cursor.fetchall()
        return product


def get_product_sub_category158(p):
    with sqlite3.connect('product.db') as db:
        cursor = db.cursor()
        cursor.execute(
            f"SELECT * FROM product WHERE Tamila = 0 and category = 'т р и к о т а ж' and sub_category = '{p}'")
        product = cursor.fetchall()
        return product

# def find_brand_db(d, *args):
#     with sqlite3.connect('product.db') as db:
#         cursor = db.cursor()
#         if len(args) > 0:
#             cursor.execute(f"""SELECT * FROM product
#             WHERE (brand = '{d}')
#             and (size LIKE '%{args[0]}%' or size LIKE '{args[0]}%'
#             or size LIKE '%{args[0]}'
#             or size LIKE '%{args[0]}%' or size LIKE '{args[0]}%' or size LIKE '%{args[0]}')""")
#             product = cursor.fetchall()
#             return product
#         else:
#             cursor.execute(f"""SELECT * FROM product
#                         WHERE brand = '{d}' """)
#             product = cursor.fetchall()
#             return product
