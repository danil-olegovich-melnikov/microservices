import time
import random

from db import tables
from db.conn import conn
from db.db_classes import Transaction
from db.sql_queries import get_products, get_users, insert_transaction

tables.create(conn)


def service1(conn):
    product = random.choice(get_products(conn))
    user = random.choice(get_users(conn))
    transaction = Transaction(
        description=product.name,
        price=product.price,
        quantity=random.randint(1, 5),
        amount=0,
        email=user.email,
    )
    insert_transaction(conn, transaction)
    return transaction


if __name__ == '__main__':
    while True:
        service1(conn)
        print("Inserted")
        time.sleep(10)
