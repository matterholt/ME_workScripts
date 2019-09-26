
import unittest
from local_packages.read_file import *
from local_packages.regex_groups import subcase_labels


class Regex_checks(unittest.TestCase):

    def reg_find_label(self):
        input_value = 'Eget duis at lat-LX tellus at urna condimentum.'
        expect = 'lat-LX'
        function_test = subcase_labels(input_value)
        self.assertEqual(function_test, expect)


if __name__ == '__main__':
    unittest.main()
