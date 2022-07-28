import unittest

from Median import find_median
from Mean import find_mean
from Range import find_range
from Mode import find_mode
from Interquartile_Range import find_interquartile_range


class Test_9G(unittest.TestCase):
    """Test exercise 9G"""

    def test_1D(self):
        self.assertEqual(find_range([1, 5, 2, 10, 3]), 9)

    def test_2A(self):
        self.assertEqual(find_range([2, 10, 1, 3, 9]), 9)

    def test_2B(self):
        self.assertEqual(find_range([6, 8, 13, 7, 1]), 12)

    def test_2C(self):
        self.assertEqual(find_range([0, 6, 3, 9, 1]), 9)

    def test_2D(self):
        self.assertEqual(find_range([3, 10, 7, 5, 10]), 7)

    def test_3B(self):
        self.assertEqual(find_mean([1, 5, 7, 7, 10]), 6)

    def test_3C(self):
        self.assertEqual(find_median([1, 5, 7, 7, 10]), 7)

    def test_3D(self):
        self.assertEqual(find_mode([1, 5, 7, 7, 10]), 7)

    def test_4AI(self):
        self.assertEqual(find_range([1, 7, 1, 2, 4]), 6)

    def test_4AII(self):
        self.assertEqual(find_mean([1, 7, 1, 2, 4]), 3)

    def test_4AIII(self):
        self.assertEqual(find_median([1, 7, 1, 2, 4]), 2)

    def test_4AIV(self):
        self.assertEqual(find_mode([1, 7, 1, 2, 4]), 1)

    def test_4BI(self):
        self.assertEqual(find_range([2, 2, 10, 8, 13]), 11)

    def test_4BII(self):
        self.assertEqual(find_mean([2, 2, 10, 8, 13]), 7)

    def test_4BIII(self):
        self.assertEqual(find_median([2, 2, 10, 8, 13]), 8)

    def test_4BIV(self):
        self.assertEqual(find_mode([2, 2, 10, 8, 13]), 2)

    def test_4CI(self):
        self.assertEqual(find_range([3, 11, 11, 14, 21]), 18)

    def test_4CII(self):
        self.assertEqual(find_mean([3, 11, 11, 14, 21]), 12)

    def test_4CIII(self):
        self.assertEqual(find_median([3, 11, 11, 14, 21]), 11)

    def test_4CIV(self):
        self.assertEqual(find_mode([3, 11, 11, 14, 21]), 11)

    def test_4DI(self):
        self.assertEqual(find_range([25, 25, 20, 37, 25, 24]), 17)

    def test_4DII(self):
        self.assertEqual(find_mean([25, 25, 20, 37, 25, 24]), 26)

    def test_4DIII(self):
        self.assertEqual(find_median([25, 25, 20, 37, 25, 24]), 25)

    def test_4DIV(self):
        self.assertEqual(find_mode([25, 25, 20, 37, 25, 24]), 25)

    def test_4EI(self):
        self.assertEqual(find_range([1, 22, 10, 20, 33, 10]), 32)

    def test_4EII(self):
        self.assertEqual(find_mean([1, 22, 10, 20, 33, 10]), 16)

    def test_4EIII(self):
        self.assertEqual(find_median([1, 22, 10, 20, 33, 10]), 15)

    def test_4EIV(self):
        self.assertEqual(find_mode([1, 22, 10, 20, 33, 10]), 10)

    def test_4FI(self):
        self.assertEqual(find_range([55, 24, 55, 19, 15, 36]), 40)

    def test_4FII(self):
        self.assertEqual(find_mean([55, 24, 55, 19, 15, 36]), 34)

    def test_4FIII(self):
        self.assertEqual(find_median([55, 24, 55, 19, 15, 36]), 30)

    def test_4FIV(self):
        self.assertEqual(find_mode([55, 24, 55, 19, 15, 36]), 55)

    def test_4GI(self):
        self.assertEqual(find_range([114, 84, 83, 81, 39, 12, 84]), 102)

    def test_4GII(self):
        self.assertEqual(find_mean([114, 84, 83, 81, 39, 12, 84]), 71)

    def test_4GIII(self):
        self.assertEqual(find_median([114, 84, 83, 81, 39, 12, 84]), 83)

    def test_4GIV(self):
        self.assertEqual(find_mode([114, 84, 83, 81, 39, 12, 84]), 84)

    def test_4HI(self):
        self.assertEqual(find_range([97, 31, 18, 54, 18, 63, 6]), 91)

    def test_4HII(self):
        self.assertEqual(find_mean([97, 31, 18, 54, 18, 63, 6]), 41)

    def test_4HIII(self):
        self.assertEqual(find_median([97, 31, 18, 54, 18, 63, 6]), 31)

    def test_4HIV(self):
        self.assertEqual(find_mode([97, 31, 18, 54, 18, 63, 6]), 18)

    def test_5A(self):
        self.assertEqual(round(find_mean([11, 18, 11, 17, 19, 22, 23, 12]), 1),
                         ANSWER)

    def test_5B(self):
        self.assertEqual(find_median([11, 18, 11, 17, 19, 22, 23, 12]), ANSWER)

    def test_5C(self):
        self.assertEqual(find_range([11, 18, 11, 17, 19, 22, 23, 12]), ANSWER)

    def test_7A(self):
        self.assertEqual(find_mean([8, 10, 8, 7, 9]), ANSWER)

    def test_7B(self):
        self.assertEqual(find_median([8, 10, 8, 7, 9]), ANSWER)

    def test_7C(self):
        self.assertEqual(find_mode([8, 10, 8, 7, 9]), ANSWER)


if __name__ == '__main__':
    unittest.main()
