from enum import Enum

"""
Classes for requests.
"""

class Status(Enum):
    NEW = 1
    READY = 2
    SEND = 3
    RECEIVE = 4
    ACCEPT = 5
    REJECT = 6


class Request:
    """"Request aggregates items, stores the status."""
    def __init__(self):
        self._items = []
        self._status = Status.NEW

    def add_item(self, item):
        self._items.append(item)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def items(self):
        return iter(self._items)
