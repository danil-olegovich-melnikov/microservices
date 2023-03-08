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


    #
    # complete_transactions(conn)
    # transactions = get_transactions(conn)
    # for transaction in transactions:
    #     assert transaction.status == "completed"


def test_service2(conn):
    for _ in range(5):
        service1(conn)

    service2()
    transactions = get_transactions(conn)
    for transaction in transactions:
        print(transaction)
        # assert transaction.status == "sending"
        # assert transaction.price * transaction.quantity == transaction.amount


def test_service3(conn):
    test_service2(conn)
    service3()
    transactions = get_transactions(conn)
    for transaction in transactions:
        assert transaction.status == "sent"
