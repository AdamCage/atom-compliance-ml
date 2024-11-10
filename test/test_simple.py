from unittest import TestCase
from test.simple import plus


class SimpleTest(TestCase):

    def test_check_simple_method_success(self):
        expected_data = 3
        actual_data = plus(1, 2)
        self.assertEqual(expected_data, actual_data)

    def test_check_simple_method_failure(self):
        expected_data = 3
        actual_data = plus(1, 3)
        self.assertNotEqual(expected_data, actual_data)