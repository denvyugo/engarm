import materials
import unittest

order_pcs = materials.OrderPieces()
order_lcs = materials.OrderLicenses()
hard = materials.Hardware(name='hard', quantity=2, cost=10, order_form=order_pcs)
soft = materials.Software(name='soft', quantity=3, cost=5, order_form=order_lcs)

class TestItems(unittest.TestCase):

    def test_hard(self):
        self.assertEqual(hard.get_info(), {'name': 'hard',
                                           'quantity': 2,
                                           'price': 24,
                                           'vat': 4})

    def test_soft(self):
        self.assertEqual(soft.price(), 15)
        self.assertEqual(soft.get_info(), {'name': 'soft',
                                           'quantity': 3,
                                           'price': 15,
                                           'vat': 'no vat'})
    def test_hard_order(self):
        self.assertEqual(hard.get_order(), 'name: hard of 2 pcs')

    def test_soft_order(self):
        self.assertEqual(soft.get_order(), 'name: soft of 3 lns')


class TestFactory(unittest.TestCase):
    def test_hardfactory(self):
        factory = materials.Hardfactory()
        self.assertEqual(isinstance(factory, materials.Itemfactory), True)

    def test_softfactory(self):
        factory = materials.Softfactory()
        self.assertEqual(isinstance(factory, materials.Itemfactory), True)

    def test_factories(self):
        factory_h = materials.Hardfactory()
        factory_s = materials.Softfactory()
        factory_p = materials.Packfactory()

        factories = []
        factories.append(factory_h)
        factories.append(factory_s)
        factories.append(factory_p)
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

        self.assertEqual(isinstance(factory_p.create_item(name='pack',
                                                          quantity=15,
                                                          cost=3), materials.Hardware), True)

        pack = factory_p.create_item(name='pack', quantity=15, cost=3, pack_val=10)
        self.assertEqual(pack.get_order(), 'name: pack of 2 pkg')
