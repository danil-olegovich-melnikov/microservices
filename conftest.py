import psycopg2
import pytest as pytest
from sqlalchemy import create_engine
from testcontainers.postgres import PostgresContainer

from db.db_classes import Transaction
from db.sql_queries import insert_transaction
from db.tables import create


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    postgres_container = PostgresContainer("postgres:9.5")
    with postgres_container as postgres:
        return postgres.get_connection_url()


@pytest.fixture()
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create(conn)
    transactions = [
        Transaction(
            description="test_description 1",
            price=1,
            quantity=10,
            amount=0,
            email='test@mail.ru'
        ),
        Transaction(
            description="test_description 2",
            price=2,
            quantity=20,
            amount=0,
            email='test@mail.ru'
        ),
        Transaction(
            description="test_description 3",
            price=3,
            quantity=30,
            amount=0,
            email='test@mail.ru'
        ),
    ]
    for transaction in transactions:
        insert_transaction(conn, transaction)
    return postgres_container.get_connection_url()


from testcontainers.postgres import PostgresContainer

with PostgresContainer('postgres:9.5') as postgres:
    postgres.get_exposed_port(5432)
    print(f"exposed port: {postgres.get_exposed_port(5432)}")
    connection_string = postgres.get_connection_url()

    connection = psycopg2.connect(
        user=postgres.POSTGRES_USER,
        password=postgres.POSTGRES_PASSWORD,
        host=postgres.get_container_host_ip(),
        port=postgres.get_exposed_port(5432),
        database=postgres.POSTGRES_DB,
    )

    cursor = connection.cursor()
    cursor.execute("""select version()""")
    row = cursor.fetchone()
