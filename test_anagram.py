"""
Author: Devin Baack
Program: test_anagram.py
Date Modified: 08/01/2020

Portions of the anagram.py program have been isolated and modified
to have parameters and return values in order to execute TestCase unit tests.
"""

import unittest


class InvalidInputException(Exception):
    pass


# Condensed, isolated version of solve_click, modified to have parameter and return value
# in order to properly test it.

anagrams = []


def solve_click(entry_word):

    dictionary = open("english3.txt").read().splitlines()

    try:
        if not entry_word.isalpha():
            raise InvalidInputException
    except InvalidInputException:
        return False

    for line in dictionary:
        if sorted(line) == sorted(entry_word.lower()):
            anagrams.append(line)

    return anagrams


# This method also clears the entry box and results label in the actual program.
# This method has been condensed for proper testing.
def clear_click(list_to_clear):
    list_to_clear.clear()
    return list_to_clear


class AnagramTestCase(unittest.TestCase):
    def test_integer_input1(self):
        self.assertEqual(solve_click("11"), False)

    def test_integer_input2(self):
        self.assertEqual(solve_click("Dev1n"), False)

    def test_solve_click1(self):
        self.assertEqual(solve_click("python"), ['phyton', 'python', 'typhon'])
        clear_click(anagrams)

    def test_solve_click2(self):
        self.assertEqual(solve_click("medical"), ['camelid', 'claimed', 'decimal', 'declaim', 'maliced', 'medical'])
        clear_click(anagrams)

    def test_solve_click3(self):
        self.assertEqual(solve_click("Hi"), ['hi'])
        clear_click(anagrams)

    def test_solve_click4(self):
        self.assertEqual(solve_click("D"), ['d'])

    def test_clear_click1(self):
        solve_click("python")
        self.assertEqual(clear_click(anagrams), [])

    def test_clear_click2(self):
        solve_click("16")
        self.assertEqual(clear_click(anagrams), [])


if __name__ == '__main__':
    unittest.main()
