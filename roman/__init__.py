from .to_decimal import _map_representation, _values_for_each_letter


def to_decimal(r: str) -> int:
    """ Return a Decimal Number by a Roman Number 'r' """
    if type(r) is not str:
        raise TypeError(f'Expect string, got {type(r)}')

    values = _values_for_each_letter(r)
    return sum(_map_representation(values))


NUMERALS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
            'IV': 4, 'I': 1}


def to_roman(d: int) -> str:
    """ Return a Roman Number by a Decimal Number 'd' """
    roman = []
    for key, value in NUMERALS.items():
        count = int(d / value)
        if count:
            roman.append(key * count)
            d -= value * count
    return ''.join(roman)
