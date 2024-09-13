import unittest
from unittest import TestCase
import main as m

class TestOne(TestCase):
    def test_get_name_1(self):
        self.assertEqual(m.get_name("10006"), "Аристарх Павлов")
    def test_get_name_2(self):
        self.assertEqual(m.get_name("311 020203"), "Александр Пушкин")
    def test_get_directory_1(self):
        self.assertEqual(m.get_directory("11-2"), "1")
    def test_get_directory_2(self):
        self.assertEqual(m.get_directory("311 020203"), "3")
    @unittest.expectedFailure
    def test_get_directory_3_fail(self):
        self.assertEqual(m.get_directory("312 020204"), "3")
    def test_add(self):
        self.assertEqual(m.add('international passport', '311 020203', 'Александр Пушкин', 3), "Добавлено")

if __name__ == '__main__':
    unittest.main()