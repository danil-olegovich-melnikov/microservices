import time

from db import tables
from db.conn import conn
from db.sql_queries import update_transactions

tables.create(conn)

if __name__ == '__main__':
    while True:
        update_transactions(conn)
        print("updated")
        time.sleep(20)
