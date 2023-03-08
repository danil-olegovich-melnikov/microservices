from testcontainers.postgres import PostgresContainer
import pytest

from db import tables
import psycopg2

@pytest.fixture()
def pql_container():
    container = PostgresContainer(image="postgres:9.5")
    container.start()
    return container


@pytest.fixture()
def conn(pql_container):
    pql_container.get_exposed_port(5432)
    connection_string = pql_container.get_connection_url()

    conn = psycopg2.connect(
        user=pql_container.POSTGRES_USER,
        password=pql_container.POSTGRES_PASSWORD,
        host=pql_container.get_container_host_ip(),
        port=pql_container.get_exposed_port(5432),
        database=pql_container.POSTGRES_DB,
    )
    tables.create(conn)
    return conn


