
import unittest
from local_packages.read_file import *


class CheckTest(unittest.TestCase):

    def test_function(self):
        input_value = 'congrats it works'
        result_expected = 'congrats it works!!!'
        function_test = read_doc(input_value)
        self.assertEqual(function_test, result_expected)


if __name__ == '__main__':
    unittest.main()
