import unittest
from unittest import TestCase
import main as m

class TestTwo(TestCase):
    def test_with_params(self):
        for i, (a, expected) in enumerate([
            ([1, 2, 3, 2, 2], 2),
            ([1, 2, 3, 1, 1], 1),
            ([1, 2, 3, 4, 4], 4),
            ([1, 1, 3, 4, 2], 1)
        ]):
            with self.subTest(i):
                result = m.vote(a)
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
