class UserException(Exception):
    pass


class WrongInputException(UserException):
    def __init__(self, place, input):
        self.place = place
        self.type = type(input)

    def __str__(self):
        return f'Price and discount must be integer! Your {self.place} is {self.type}'


class WrongPriceException(UserException):
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'Price cant be negative or 0! Your price is {self.price}!'


class WrongDiscountException(UserException):
    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'Discount must be between 0 and 100%! Your discount is {self.discount}%!'
