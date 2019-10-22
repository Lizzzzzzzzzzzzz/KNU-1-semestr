from unittest import TestCase
import unittest
from main import y

class TestValue(TestCase):
    def test_value(self):
        self.assertEqual(y(x), "nan")



if __name__ == "__main__":
    unittest.main()



