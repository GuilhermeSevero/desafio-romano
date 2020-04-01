

NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def _values_for_each_letter(r: str) -> list:
    """ Return a list that have a value representation of each letter """
    return [NUMERALS[i] for i in r.upper()]


def _map_representation(r: list) -> list:
    """ Map values to add or subtract """
    return [value if value >= r[min(index + 1, len(r) - 1)] else -value for index, value in enumerate(r)]
