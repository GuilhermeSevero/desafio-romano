
NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def to_decimal(r: str) -> int:
    """Return a Decimal Number by a Roman Number 'r'"""
    decimal = 0
    for index, letter in enumerate(r):
        value = NUMERALS.get(letter.upper(), 0)
        if value >= NUMERALS.get(r[min(index + 1, len(r) - 1)]):
            decimal += value
        else:
            decimal -= value
    return decimal
