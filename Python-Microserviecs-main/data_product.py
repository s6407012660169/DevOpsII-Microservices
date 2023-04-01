import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_products.db")

# get products
def get_products():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM products
        ORDER BY id
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        record = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3],
            'instock': row[4]
        }
        data.append(record)
    conn.close()
    return data

# get product by id
def get_product(id):
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT *
        FROM products
        WHERE id=?
    """
    val = (id,)
    cursor = conn.execute(sql, val)
    columns = cursor.fetchone()
    record = {
        'id': columns[0],
        'name': columns[1],
        'category': columns[2],
        'price': columns[3],
        'instock': columns[4],
    }
    conn.close()
    return record

# add product
def add_product(name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO products(name, category, price, instock)
        VALUES(?, ?, ?, ?)
    """
    val = (name, category, price, instock, )
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

# delete product
def delete_product(id):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM products
        WHERE id=?
    """
    val = (id)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return 'Deleted successfully'

# update product
def update_product(id, name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE products
        SET name=?, category=?, price=?, instock=?
        WHERE id=?
    """
    val = (name, category, price, instock, id)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Updated successfully"

