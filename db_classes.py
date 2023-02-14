from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    description: str
    price: int
    quantity: int
    amount: int
    email: str
    created: str = ""
    check_status: str = "un_send"
    id: Optional[int] = None

    @staticmethod
    def list_transactions(transactions: []):
        return [Transaction(id=transaction[0], description=transaction[1],
                            price=transaction[2], amount=transaction[3],
                            quantity=transaction[4], email=transaction[5],
                            created=transaction[6], check_status=transaction[7])
                for transaction in transactions]


@dataclass
class User:
    username: str
    password: str
    email: str
    id: Optional[int] = None


@dataclass
class Product:
    name: str
    price: int
    id: Optional[int] = None
