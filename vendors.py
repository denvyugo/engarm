
"""
Classes for vendors.
"""

class Vendor:

    def __init__(self, name):
        self._name = name
        self._contact = None

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def name(self):
        return self._name


class Contact:

    def __init__(self):
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
