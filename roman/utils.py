

NUMERALS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
            'IV': 4, 'I': 1}


def _values_for_each_letter(r: str) -> list:
    """ Return a list that have a value representation of each letter """
    return [NUMERALS[i] for i in r.upper()]


def _map_representation(r: list) -> list:
    """ Map values to add or subtract """
    return [value if value >= r[min(index + 1, len(r) - 1)] else -value for index, value in enumerate(r)]


def _calc_letters(d: int) -> dict:
    """ Calculate how many letter are needed """
    romans = {}
    for key, value in NUMERALS.items():
        romans[key] = int(d / value)
        d -= value * romans[key]
    return romans
