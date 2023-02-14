import time
import random
import sql_queries
import tables
from db_classes import Transaction

tables.create()


if __name__ == '__main__':
    while True:
        product = random.choice(sql_queries.get_products())
        user = random.choice(sql_queries.get_users())
        sql_queries.insert_transaction(
            Transaction(
                description=product.name,
                price=product.price,
                quantity=random.randint(1, 5),
                amount=0,
                email=user.email,
            )
        )
        print("Inserted")
        time.sleep(10)
