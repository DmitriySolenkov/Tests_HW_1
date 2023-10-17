from Calculator import calculation_discount
from Exceptions import WrongDiscountException, WrongInputException, WrongPriceException
import unittest


class TestExample(unittest.TestCase):

    def test1(self):
        self.assertRaises(WrongPriceException, calculation_discount, -5, 50)

    def test2(self):
        self.assertRaises(WrongDiscountException,
                          calculation_discount, 100, 100)

    def test3(self):
        self.assertRaises(WrongDiscountException,
                          calculation_discount, 100, -10)

    def test4(self):
        self.assertRaises(WrongInputException,
                          calculation_discount, 100, "string")

    def test5(self):
        self.assertRaises(WrongInputException,
                          calculation_discount, "string", 100)

    def test6(self):
        self.assertEqual(calculation_discount(50, 50), 25)

    def test7(self):
        self.assertEqual(calculation_discount(100, 15), 85)


if __name__ == '__main__':
    unittest.main()
