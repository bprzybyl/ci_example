# Brooks Przybylek
# CS_362_C400_S2020 A2: TDD Hands On
# 05/12/2020
#
# This testing suite is meant to test the following requirements:
#   check_pwd accepts a string and returns True if it meets the criteria
#   listed below, otherwise it returns False:
#
# - Must be between 8 and 20 characters (inclusive)
# - Must contain at least one lowercase letter
# - Must contain at least one uppercase letter
# - Must contain at least one digit
# - Must contain at least one symbol from: ~`!@#$%^&*()_+-=
# - You may assume that only strings will be sent to the check_pwd.

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testLengthRequirement(self):
        self.assertFalse(check_pwd("aB1#"))

    def testLowercaseLetterRequirement(self):
        self.assertFalse(check_pwd("AB%2CD(3"))

    def testUppercaseLetterRequirement(self):
        self.assertFalse(check_pwd("ab@4cd$5ef)6gh^7"))

    def testDigitRequirement(self):
        self.assertFalse(check_pwd("iEI~jFJ`kGK&lHL_"))

    def testSpecialCharacterRequirement(self):
        self.assertFalse(check_pwd("Mm8qNn9QOo0rPp1R"))


if __name__ == '__main__':
    unittest.main()
