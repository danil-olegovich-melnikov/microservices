import time

from db import tables
from db.conn import conn
from db.sql_queries import get_transactions

tables.create(conn)


if __name__ == '__main__':
    while True:
        transactions = get_transactions(conn)
        print("-------------------- >>")
        for transaction in transactions:
            print(transaction)
        print("-------------------- <<")
        time.sleep(8)
