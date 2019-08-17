import abc

"""
Classes of materials items: hardware & software
Hardware orders by pieces or in packages.
Software orders by licenses.
"""


"""Abstract Factory pattern for create items"""

class Itemfactory(metaclass=abc.ABCMeta):
    """Abstract Factory class"""
    @abc.abstractmethod
    def create_item(self, **kwargs):
        pass


class Hardfactory(Itemfactory):
    """Factory that creates a hardware that ordered by pieces"""
    def create_item(self, name, quantity, cost):
        order_form = OrderPieces()
        return Hardware(name=name, quantity=quantity, cost=cost, order_form=order_form)


class Packfactory(Itemfactory):
    """Factory that creates a hardware that ordered by packages"""
    def create_item(self, name, quantity, cost, **kwargs):
        order_form = OrderPackages()
        if 'pack_val' in kwargs:
            order_form.packvalue(kwargs['pack_val'])
        return Hardware(name=name, quantity=quantity, cost=cost, order_form=order_form)


class Softfactory(Itemfactory):
    """Factory that creates a software that ordered by licenses"""
    def create_item(self, name, quantity, cost):
        order_form = OrderLicenses()
        return Software(name=name, quantity=quantity, cost=cost, order_form=order_form)


class Item(metaclass=abc.ABCMeta):
    """
    Abstract class for describe item interface.
    Item has an order_form object which implement Bridge pattern for order in right units (pcs, pkg, lns)
    """

    DEFAULT_VAT = 0.2

    def __init__(self, name, quantity, cost, order_form):
        self._name = name
        self._quantity = quantity
        self._cost = cost
        self._vat = __class__.DEFAULT_VAT
        self._order_form = order_form

    def price(self):
        return self._cost * self._quantity * (1 + self._vat)

    def get_order(self):
        return self._order_form.get_order(self._name, self._quantity)

    @abc.abstractmethod
    def get_info(self):
        pass


class Hardware(Item):
    def __init__(self, name, quantity, cost, order_form):
        super().__init__(name, quantity, cost, order_form)
        self._vat = 0.2

    def get_info(self):
        return {'name': self._name,
                'quantity': self._quantity,
                'price': self.price(),
                'vat': self._quantity * self._cost * self._vat}


class Software(Item):
    def __init__(self, name, quantity, cost, order_form):
        super().__init__(name, quantity, cost, order_form)
        self._vat = 0.0

    def get_info(self):
        return {'name': self._name, 'quantity': self._quantity, 'price': self.price(), 'vat': 'no vat'}


"""Bridge pattern"""

class OrderForm(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_order(self, **kwargs):
        pass


class OrderPieces(OrderForm):

    def get_order(self, name, quantity):
        return f'name: {name} of {quantity} pcs'


class OrderLicenses(OrderForm):

    def get_order(self, name, quantity):
        return f'name: {name} of {quantity} lns'


class OrderPackages(OrderForm):
    DEFAULT_PACK = 1

    def __init__(self,):
        self._pcs_in_pack = __class__.DEFAULT_PACK

    def packvalue(self, pcs_in_pack):
        self._pcs_in_pack = pcs_in_pack

    def get_order(self, name, quantity):
        number_packs = quantity // self._pcs_in_pack
        if quantity % self._pcs_in_pack:
            number_packs += 1
        return f'name: {name} of {number_packs} pkg'

