import unittest
from python_repos import get_code, get_number_of_repos


class TestRepos(unittest.TestCase):

    def test_staus_code_1(self):
        self.assertEqual(get_code(), 200)

    def test_status_code_2(self):
        self.assertNotEqual(get_code(), 300)

    def test_get_number_of_repos_1(self):
        self.assertGreaterEqual(get_number_of_repos(), 4675036)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
