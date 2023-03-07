from db.db_classes import Transaction
from db.sql_queries import insert_transaction, get_transactions, update_transactions, complete_transactions
from service1 import service1


def test_service1(postgres_conn):
    transaction = service1(postgres_conn)
    print(transaction)
    # insert_transaction(conn, transaction)
    #
    # transactions = get_transactions(conn)
    # assert len(transactions) == 4
    # transaction = transactions[-1]
    # assert transaction.description == "test_description"
    #
    # update_transactions(conn)
    # transactions = get_transactions(conn)
    # for transaction in transactions:
    #     assert transaction.price * transaction.quantity == transaction.amount
    #     assert transaction.status == "calculated"
    #
    # complete_transactions(conn)
    # transactions = get_transactions(conn)
    # for transaction in transactions:
    #     assert transaction.status == "completed"
