import time
import tables
import sql_queries
from db_classes import Transaction

tables.create()

if __name__ == '__main__':
    while True:
        transactions: list[Transaction] = sql_queries.get_sending_transaction()
        for transaction in transactions:
            print(f"Sending email to {transaction.email} - total amount of purchase is {transaction.amount}")
            time.sleep(2)
        sql_queries.complete_transactions()
        print("completed")
        time.sleep(20)
