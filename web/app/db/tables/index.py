from enum import Enum


class Table(Enum):
    USER = 1
    SERVICE = 2
    PHONE = 3
    SERVICE_PROVIDER = 4
    SERVICE_CONTRACTOR = 5
    SERVICE_REQUEST = 6
    FEEDBACK = 7


class QueryType(Enum):
    SELECT = ("SELECT", "END-SELECT")
    SELECT_MANY = ("SELECT_MANY", "END-SELECT_MANY")
    INSERT = ("INSERT", "END-INSERT")
    UPDATE = ("UPDATE", "END-UPDATE")
    DELETE = ("DELETE", "END-DELETE")
