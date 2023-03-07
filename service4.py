import time

from db import tables
from db.conn import conn
from db.sql_queries import get_transactions

tables.create(conn)

def service4():
    transactions = get_transactions(conn)
    print("-------------------- >>")
    for transaction in transactions:
        print(transaction)
    print("-------------------- <<")
    time.sleep(8)


if __name__ == '__main__':
    while True:
       service4()
