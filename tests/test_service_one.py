from sqlalchemy import create_engine

from db import conn
from db.db_classes import Transaction
from db.sql_queries import insert_transaction, get_transactions, update_transactions, complete_transactions


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    transaction = Transaction(
        description="test_description",
        price=100,
        quantity=1000,
        amount=0,
    )
    insert_transaction(conn, transaction)

    transactions = get_transactions(conn)
    assert len(transactions) == 4
    transaction = transactions[-1]
    assert transaction.description == "test_description"

    update_transactions(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.price * transaction.quantity == transaction.amount
        assert transaction.status == "calculated"

    complete_transactions(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.status == "completed"