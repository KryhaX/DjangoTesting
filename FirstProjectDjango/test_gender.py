from unittest import TestCase

import gender


class Test(TestCase):
    def test_converter_when_male(self):
        actual = gender.converter("M")
        expected = "MALE"
        self.assertEqual(actual, expected)
