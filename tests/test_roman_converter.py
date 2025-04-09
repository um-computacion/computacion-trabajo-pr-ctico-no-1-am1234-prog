import unittest 
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(decimal_to_roman(1), "I")

    def test_cinco(self):
        self.assertEqual(decimal_to_roman(5), "V")

    def test_diez(self):
        self.assertEqual(decimal_to_roman(10), "X")

    def test_cuatro(self):
        self.assertEqual(decimal_to_roman(4), "IV")

    def test_nueve(self):
        self.assertEqual(decimal_to_roman(9), "IX")

    def test_cuarenta_y_nueve(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")

    def test_tres_mil_novecientos_noventa_y_nueve(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")
        
    def test_cero(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(-1)

    def test_mayor_a_3999(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)



if __name__ == "__main__":
    unittest.main()

