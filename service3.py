import time

from db import tables
from db.conn import conn
from db.sql_queries import get_sending_transaction, complete_transactions

tables.create(conn)


def service3():
    transactions = get_sending_transaction(conn)
    for transaction in transactions:
        print(f"Sending email to {transaction.email} - total amount of purchase is {transaction.amount}")
        time.sleep(2)
    complete_transactions(conn)


if __name__ == '__main__':
    while True:
        service3()
        time.sleep(20)
