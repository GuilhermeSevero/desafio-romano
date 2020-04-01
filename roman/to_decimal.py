

NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def _values_for_each_letter(r: str) -> list:
    """ Return a list that have a value representation of each letter """
    return [NUMERALS[i] for i in r.upper()]


def _map_representation(r: list) -> list:
    """ Map values to add or subtract """
    return [i if i >= r[min(j + 1, len(r) - 1)] else -i for j, i in enumerate(r)]
