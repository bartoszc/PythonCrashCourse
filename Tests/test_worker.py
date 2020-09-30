import unittest
from worker import Employee


class TestWorker(unittest.TestCase):

    def setUp(self):
        self.worker1 = Employee('Bartosz', 'Chojnacki', 10000)
        self.year_sum = [15000, 17000]

    def test_give_default_raise(self):
        self.worker1.give_raise()
        self.assertEqual(self.year_sum[0], self.worker1.year_revenue)

    def test_give_custom_raise(self):
        self.worker1.give_raise(7000)
        self.assertEqual(self.year_sum[1], self.worker1.year_revenue)


unittest.main(argv=['first-arg-is-ignored'], exit=False)