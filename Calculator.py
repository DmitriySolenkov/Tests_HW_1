from Exceptions import WrongPriceException, WrongDiscountException, WrongInputException


def calculation_discount(price, discount):
    if not isinstance(price, int):
        raise WrongInputException('price', price)
    if not isinstance(discount, int):
        raise WrongInputException('discount', discount)
    if price > 0:
        if (0 < discount < 100):
            return price*(100-discount)/100
        else:
            raise WrongDiscountException(discount)
    else:
        raise WrongPriceException(price)


# print(calculation_discount(100, 50))
# print(calculation_discount(100, 15))
# print(calculation_discount(70, 125))
# print(calculation_discount(-5, 25))
# print(calculation_discount('de', 50))
