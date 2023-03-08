from db.db_classes import Transaction
from db.sql_queries import insert_transaction, get_transactions, update_transactions, complete_transactions
from service1 import service1
from service2 import service2
from service3 import service3


def test_service1(conn):
    transaction = service1(conn)
    transactions = get_transactions(conn)
    assert len(transactions) == 1
    assert transactions[0].description == transaction.description


def test_service2(conn):
    for _ in range(5):
        service1(conn)

    service2(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.check_status == "sending"
        assert transaction.price * transaction.amount == transaction.quantity


def test_service3(conn):
    test_service2(conn)
    service3(conn)
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.check_status == "sent"


def test_show_error():
    assert 1 != 0
