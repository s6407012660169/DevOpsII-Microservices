import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_user.db")
# db_folder = 'C:\Users\5A09-02\Desktop\Devops\Python-Microserviecs-main\db_user.db'

def user_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT user, password , name
        FROM username 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'user': row[0],
            'password': row[1],
            'name': row[2]
            }
        data.append(record)
    
    conn.close()
    return data

def find_username(user):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT user, password , name
        FROM username 
        WHERE user=?
    """
    val = (user,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'user': rows[0],
        'password': rows[1],
        'name': rows[2]
        }
    data.append(record)
    
    conn.close()
    return data

def user_name_add(user,passwd,name):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO username(user,password,name)
        VALUES(?,?,?)
    """
    val = (user,passwd,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

#delete
def delete_user(user):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM username
        WHERE user=?
    """
    val = (user,)
    cursor = conn.execute(sql,val)
    conn.commit()
    conn.close()
    return 'Deleted successfully'

#put
def update_user(user,passwd,name):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE username
        SET password=?, name=?
        WHERE user=?
    """
    val = (passwd,name,user)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Updated successfully"

