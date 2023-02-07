import unittest

from RomanConvertor import RomanConvertor

class TestRomanConvertor(unittest.TestCase) :

    def test_one_is_one(self):
        one = "1"

        oneRoman = RomanConvertor.convert(one)

        self.assertEqual(oneRoman,"I")

    def test_two_is_two(self):
        two = "2"

        twoRoman = RomanConvertor.convert(two)

        self.assertEqual(twoRoman, "II")
    
    def test_three_is_three(self):
        three = "3"

        threeRoman = RomanConvertor.convert(three)

        self.assertEqual(threeRoman, "III")
