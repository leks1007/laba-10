import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_vutratu(conn):
    sql = 'SELECT * FROM vutratu'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_vutratu(conn, task):
    sql = ''' INSERT INTO vutratu (Name, Value, Date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


def update_vutratu(conn, data):
    sql = ''' UPDATE vutratu
              SET Value = ?
              WHERE Name = ? AND Date = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def remove_vutratu(conn, removed_task):
    sql = ''' DELETE FROM vutratu WHERE Name = ? AND Value = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


def main():

    database = r"rubchyk.db" 
 
    conn = create_connection(database)

    with conn:
        print("\nВсі витрати (назва, вартість, дата)")
        select_vutratu(conn)
        print("\nВставка нового рядка...")
        create_vutratu(conn, ('Зимовий одяг', '3000', '01.12.2019'))
        print("\nВсі витрати (назва, вартість, дата)")
        select_vutratu(conn)
        print("\nЗміна рядка...")
        update_vutratu(conn, ('Зимовий одяг', '5000', '10.12.2019'))
        print("\nВсі витрати (назва, вартість, дата)")
        select_vutratu(conn)
        print("\nВидалення рядка")
        remove_vutratu(conn, ('Зимовий одяг', '5000'))
        print("\nВсі витрати (назва, вартість, дата)")
        select_vutratu(conn)
        
 
if __name__ == '__main__':
    main()
