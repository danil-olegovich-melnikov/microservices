import random
import uuid
from db.db_classes import Transaction, Product, User


def create_table_transaction(conn):
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


def create_table_product(conn):
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
    if len(get_products(conn)) == 0:
        insert_products(conn)


def create_table_user(conn):
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
    if len(get_users(conn)) == 0:
        insert_users(conn)


def insert_users(conn):
    for _ in range(100):
        query = """
        INSERT INTO m_danil_user (username, password, email)
        VALUES (%s, %s, %s)
        """

        user = uuid.uuid4().hex
        cursor = conn.cursor()
        cursor.execute(query, (user[:8], user[8:20], user[20:32] + "@mail.ru"))
        conn.commit()


def insert_products(conn):
    for _ in range(100):
        query = """
        INSERT INTO m_danil_product (name, price)
        VALUES (%s, %s)
        """

        product = uuid.uuid4().hex
        cursor = conn.cursor()
        cursor.execute(query, (product[:10], random.randint(1, 100) * 1000))
        conn.commit()


def get_users(conn):
    query = "SELECT * FROM m_danil_user;"
    cursor = conn.cursor()
    cursor.execute(query)

    return [User(username=user[2], password=user[3], email=user[1], id=user[0])
            for user in cursor.fetchall()]


def get_products(conn):
    query = "SELECT * FROM m_danil_product;"
    cursor = conn.cursor()
    cursor.execute(query)

    return [Product(name=product[1], id=product[0], price=product[2])
            for product in cursor.fetchall()]


def insert_transaction(conn, transaction: Transaction):
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


def update_transactions(conn):
    query = "UPDATE m_danil_transaction SET amount=price*quantity, check_status='sending' WHERE check_status='un_send';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_transactions(conn):
    query = "UPDATE m_danil_transaction SET check_status='sent' WHERE check_status='sending';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_transactions(conn):
    query = "SELECT * FROM m_danil_transaction;"
    cursor = conn.cursor()
    cursor.execute(query)
    return Transaction.list_transactions(cursor.fetchall())


def get_sending_transaction(conn):
    query = "SELECT * FROM m_danil_transaction WHERE check_status='sending'"
    cursor = conn.cursor()
    cursor.execute(query)
    return Transaction.list_transactions(cursor.fetchall())
