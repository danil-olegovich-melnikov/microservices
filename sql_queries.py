import random
import uuid

from conn import conn
from db_classes import Transaction, Product, User


def create_table_transaction():
    query = """
    CREATE TABLE IF NOT EXISTS m_danil_transaction (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        email VARCHAR(255) NOT NULL,
        created DATE DEFAULT NOW(),
        check_status VARCHAR(255) DEFAULT 'un_send'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def create_table_product():
    query = """
    CREATE TABLE IF NOT EXISTS m_danil_product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def create_table_user():
    query = """
    CREATE TABLE IF NOT EXISTS m_danil_user (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_users():
    for _ in range(100):
        query = """
        INSERT INTO m_danil_user (username, password, email)
        VALUES (%s, %s, %s)
        """

        user = uuid.uuid4().hex
        cursor = conn.cursor()
        cursor.execute(query, (user[:8], user[8:20], user[20:32] + "@mail.ru"))
        conn.commit()


def insert_products():
    for _ in range(100):
        query = """
        INSERT INTO m_danil_product (name, price)
        VALUES (%s, %s)
        """

        product = uuid.uuid4().hex
        cursor = conn.cursor()
        cursor.execute(query, (product[:10], random.randint(1, 100) * 1000))
        conn.commit()


def get_users() -> list[User]:
    query = "SELECT * FROM m_danil_user;"
    cursor = conn.cursor()
    cursor.execute(query)

    return [User(username=user[2], password=user[3], email=user[1], id=user[0])
            for user in cursor.fetchall()]


def get_products() -> list[Product]:
    query = "SELECT * FROM m_danil_product;"
    cursor = conn.cursor()
    cursor.execute(query)

    return [Product(name=product[1], id=product[0], price=product[2])
            for product in cursor.fetchall()]


def insert_transaction(transaction: Transaction):
    query = """
    INSERT INTO m_danil_transaction (description, price, quantity, amount, email)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (
        transaction.description,
        transaction.price,
        transaction.quantity,
        transaction.amount,
        transaction.email
    ))
    conn.commit()


def update_transactions():
    query = "UPDATE m_danil_transaction SET amount=price*quantity, check_status='sending' WHERE check_status='un_send';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def complete_transactions():
    query = "UPDATE m_danil_transaction SET check_status='sent' WHERE check_status='sending';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_transactions() -> list[Transaction]:
    query = "SELECT * FROM m_danil_transaction;"
    cursor = conn.cursor()
    cursor.execute(query)
    return Transaction.list_transactions(cursor.fetchall())


def get_sending_transaction():
    query = "SELECT * FROM m_danil_transaction WHERE check_status='sending'"
    cursor = conn.cursor()
    cursor.execute(query)
    return Transaction.list_transactions(cursor.fetchall())