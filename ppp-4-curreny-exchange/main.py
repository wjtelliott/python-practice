class Currency:
    currencies = {
        'CHF': 0.930023, # swiss franc
        'CAD': 1.264553, # canadian dollar
        'GBP': 0.737414, # british pound
        'JPY': 111.019919, # japanese yen
        'EUR': 0.862361, # euro
        'USD': 1.0 # US dollar
    }

    def __init__(self, value, unit = "USD") -> None:
        self.value = value
        self.unit = unit

    def exchangeRate(_, unit_a_value, unit_a, unit_b) -> int:
        # made this using the given changeTo to make this easier later
        return (unit_a_value / Currency.currencies[unit_a] * Currency.currencies[unit_b])

    def changeTo(self, new_unit):
        """
        Current object is transformed from the unit self.unit to new_unit
        """
        self.value = self.exchangeRate(self.value, self.unit, new_unit)
        self.unit = new_unit

    def __repr__(self) -> str:
        # Return the string to be printed.
        # The value rounded to two digits, accompanied by its acronym
        return "{:.2f} {}".format(self.value, self.unit)

    def __str__(self) -> str:
        # uhhh??? whats the difference
        return self.__repr__()


    def __add__(self, other):
        new_value = 0
        if isinstance(other, int) or isinstance(other, float):
            new_value = other * Currency.currencies[self.unit] + self.value
        elif isinstance(other, Currency):
            new_value = self.exchangeRate(other.value, other.unit, self.unit) + self.value
        else: return -1 # Error, cannot add types
        return Currency(new_value, self.unit)

    def __radd__(self, other):
        # We are on the right side, and an int or float should be on the left
        # We should be able to just add like this and use __add__? Then change to USD?
        result = self + other
        result.changeTo('USD')
        return result
    
    def __iadd__(self, other):
        return Currency.__add__(self, other) # this is the same function???

    def __sub__(self, other):
        # same as add, just subtract
        new_value = 0
        if isinstance(other, int) or isinstance(other, float):
            # We need to make sure we subtract self - value, not the other way
            new_value = self.value - other * Currency.currencies[self.unit]
        elif isinstance(other, Currency):
            new_value = self.value - self.exchangeRate(other.value, other.unit, self.unit)
        else: return -1 # Error, cannot add types
        return Currency(new_value, self.unit)
    def __isub__(self, other):
        return Currency.__sub__(self, other)

    def __rsub__(self, other):
        #result = self - other
        #result.changeTo('USD')
        # This did not work...
        # subtraction order matters (oops!) I could return the -value, but instead i will subtract value correctly

        result = Currency(other, self.unit) - self
        result.changeTo('USD')
        return result


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")

print('Currency 1: ', v1)
print('Currency 2: ', v2)
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)
print(3 + v1)
print(v1 - 3)
print(30 - v2)

"""
Expected output:
40.65 EUR
47.14 USD
26.02 EUR
30.17 USD
20.84 EUR
10.03 USD
"""