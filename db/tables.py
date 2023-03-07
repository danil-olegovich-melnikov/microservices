from db import sql_queries


def create(conn):
    sql_queries.create_table_user(conn)
    sql_queries.create_table_product(conn)
    sql_queries.create_table_transaction(conn)

