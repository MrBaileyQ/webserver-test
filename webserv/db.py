def execute_sql(sql):
    import sqlite3
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return cursor