import materials
import unittest


class Test(unittest.TestCase):

    def test_hard(self):
        hard = materials.Hardware(name='hard', quantity=2, cost=10)
        self.assertEqual(hard.price(), 24)
        self.assertEqual(hard.get_info(), {'name': 'hard',
                                           'quantity': 2,
                                           'price': 24,
                                           'vat': 4})

    def test_soft(self):
        soft = materials.Software(name='soft', quantity=3, cost=5)
        self.assertEqual(soft.price(), 15)
        self.assertEqual(soft.get_info(), {'name': 'soft',
                                           'quantity': 3,
                                           'price': 15,
                                           'vat': 'no vat'})

    def test_hardfactory(self):
        factory = materials.Hardfactory()
        self.assertEqual(isinstance(factory, materials.Itemfactory), True)

    def test_softfactory(self):
        factory = materials.Softfactory()
        self.assertEqual(isinstance(factory, materials.Itemfactory), True)

    def test_factories(self):
        factory_h = materials.Hardfactory()
        factory_s = materials.Softfactory()

        factories = []
        factories.append(factory_h)
        factories.append(factory_s)
        for factory in factories:
            self.assertEqual(isinstance(factory.create_item(name='item', quantity=2, cost=3), materials.Item), True)

        self.assertEqual(isinstance(factory_h.create_item(name='item1',
                                                          quantity=1,
                                                          cost=3), materials.Hardware), True)

        self.assertEqual(isinstance(factory_h.create_item(name='item1',
                                                          quantity=1,
                                                          cost=3), materials.Software), False)

        self.assertEqual(isinstance(factory_s.create_item(name='soft',
                                                          quantity=1,
                                                          cost=3), materials.Software), True)

        self.assertEqual(isinstance(factory_s.create_item(name='soft',
                                                      quantity=1,
                                                      cost=3), materials.Hardware), False)