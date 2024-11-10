import unittest

from test.test_simple import plus


class SimpleTest2(unittest.TestCase):

    def test_check_simple_method_success2(self):
        expected_data = 3
        actual_data = plus(1, 2)
        self.assertEqual(expected_data, actual_data)

    def test_check_simple_method_failure2(self):
        expected_data = 3
        actual_data = plus(1, 3)
        self.assertNotEqual(expected_data, actual_data)
