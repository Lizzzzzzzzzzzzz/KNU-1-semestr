from unittest import TestCase
import unittest
import laba3



class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(laba3.sum(), 3.8583333333333334)



if __name__ == "__main__":
    unittest.main()

