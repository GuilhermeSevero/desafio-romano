
NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def to_decimal(r: str) -> int:
    """ Return a Decimal Number by a Roman Number 'r' """
    values = [NUMERALS[i] for i in r.upper()]
    return sum([i if i >= values[min(j + 1, len(values) - 1)] else -i for j, i in enumerate(values)])
