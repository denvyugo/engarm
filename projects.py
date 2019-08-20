from materials import Hardfactory, Hardware, OrderPackages, OrderPieces, OrderLicenses, \
    Packfactory, Softfactory, Software
from requests import Request, Status
from vendors import Contact, Vendor
from datas import ProjectData, EngarmDB

"""
Classes for work with projects, vendors, contacts
"""

class Project:
    """
    Class of project objects.
    Project object aggregates items, requests.
    Project object implements a Mediator pattern.
    Project aggregates a Data Mapper objects: EngarmDB, ProjectData
    """

    def __init__(self):
        self._prjdb = ProjectData()
        self._items = []
        self._requests = []
        self._db = EngarmDB()

    def fetch_items(self):
        pass

    def add_item(self, item):
        self._items.append(item)

    # methods of Data Mapper for project object
    def new_project(self, project_name):
        self._prjdb.name = project_name
        self._db.add_project(self._prjdb)

    def save_project(self):
        self._db.upd_project(self._prjdb)
