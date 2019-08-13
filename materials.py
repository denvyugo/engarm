import abc

DEFAULT_VAT = 0.2

class Itemfactory(metaclass=abc.ABCMeta):
    """Abstract Factory class for create items: hardware & software"""

    @abc.abstractmethod
    def create_item(self):
        pass


class Item(metaclass=abc.ABCMeta):
    """Abstract class for describe item interface"""
    def __init__(self, name, quantity, cost):
        self._name = name
        self._quantity = quantity
        self._cost = cost
        self._vat = DEFAULT_VAT

    def price(self):
        return self._cost * self._quantity * (1 + self._vat)

    @abc.abstractmethod
    def get_info(self):
        pass


class Hardware(Item):
    def __init__(self, name, quantity, cost):
        super().__init__(name, quantity, cost)
        self._vat = 0.2

    def get_info(self):
        return {'name': self._name,
                'quantity': self._quantity,
                'price': self.price(),
                'vat': self._quantity * self._cost * self._vat}


class Software(Item):
    def __init__(self, name, quantity, cost):
        super().__init__(name, quantity, cost)
        self._vat = 0.0

    def get_info(self):
        return {'name': self._name, 'quantity': self._quantity, 'price': self.price(), 'vat': 'no vat'}


