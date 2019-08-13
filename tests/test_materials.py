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