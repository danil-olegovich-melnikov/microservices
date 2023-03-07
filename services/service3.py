import time

from db import tables
from db.conn import conn
from db.db_classes import Transaction
from db.sql_queries import get_sending_transaction, complete_transactions

tables.create(conn)

if __name__ == '__main__':
    while True:
        transactions: list[Transaction] = get_sending_transaction(conn)
        for transaction in transactions:
            print(f"Sending email to {transaction.email} - total amount of purchase is {transaction.amount}")
            time.sleep(2)
        complete_transactions(conn)
        time.sleep(20)
