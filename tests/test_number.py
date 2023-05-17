import unittest

from src.roman_num import roman_num


class Roman_roman_num_TestCase(unittest.TestCase):

    def test_python_test_setup_works(self):
        self.assertTrue(True)

    def test_it_returns_I_when_roman_num_is_1(self):
        # Arrange / Given

        # Act / When
        result = roman_num(1)

        # Assert / Then
        self.assertEqual('I', result)

    def test_it_returns_II_when_roman_num_is_2(self):
        # Arrange / Given

        # Act / When
        result = roman_num(2)

        # Assert / Then
        self.assertEqual('II', result)

    def test_it_returns_III_when_roman_num_is_3(self):
        # Arrange / Given

        # Act / When
        result = roman_num(3)

        # Assert / Then
        self.assertEqual('III', result)

    def test_it_returns_IV_when_roman_num_is_4(self):
        # Arrange / Given

        # Act / When
        result = roman_num(4)

        # Assert / Then
        self.assertEqual('IV', result)