import time
import sql_queries
import tables

tables.create()


if __name__ == '__main__':
    while True:
        transactions = sql_queries.get_transactions()
        print("-------------------- >>")
        for transaction in transactions:
            print(transaction)
        print("-------------------- <<")
        time.sleep(10)
