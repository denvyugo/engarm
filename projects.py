
"""
Classes for work with projects, vendors, contacts
"""

class Project:
    """
    Class of project objects.
    Project object aggregates items, requests.
    Project object implements a Mediator pattern.
    """

    def __init__(self):
        self._items = []
        self._requests = []

    def fetch_items(self):
        pass

    def add_item(self, item):
        self._items.append(item)
