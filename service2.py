import time

from db import tables
from db.conn import conn
from db.sql_queries import update_transactions

tables.create(conn)


def service2(conn):
    update_transactions(conn)


if __name__ == '__main__':
    while True:
        service2(conn)
        print("updated")
        time.sleep(20)
