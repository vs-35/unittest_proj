import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([], 1) , [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])

    def test_slise_Syntax(self):
        with self.assertRaises(NameError):
            arrs.my_slice([1, 2, 3, 4], a, b)

