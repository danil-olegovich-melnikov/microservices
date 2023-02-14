import time
import tables
from sql_queries import update_transactions

tables.create()

if __name__ == '__main__':
    while True:
        update_transactions()
        print("updated")
        time.sleep(20)
