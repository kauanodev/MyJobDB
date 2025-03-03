from enum import Enum


class Table(Enum):
    USER = 1
    SERVICE = 2
    SERVICE_PROVIDER = 4


class QueryType(Enum):
    SELECT = ("SELECT", "END-SELECT")
    SELECT_MANY = ("SELECT_MANY", "END-SELECT_MANY")
    INSERT = ("INSERT", "END-INSERT")
    UPDATE = ("UPDATE", "END-UPDATE")
    DELETE = ("DELETE", "END-DELETE")
