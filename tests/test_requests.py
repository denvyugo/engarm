import requests
import unittest

class Test(unittest.TestCase):

    def test_status(self):
        req = requests.Request()
        self.assertEqual(req.status, requests.Status.NEW)
        req.status = requests.Status.READY
        self.assertEqual(req.status, requests.Status.READY)

    def test_iter(self):
        req = requests.Request()
        for i in range(3):
            req.add_item('itm' + str(i))

        i = 0
        for itm in req.items():
            self.assertEqual(itm, 'itm' + str(i))
            i += 1