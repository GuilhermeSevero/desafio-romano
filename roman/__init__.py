from .to_decimal import _map_representation, _values_for_each_letter


def to_decimal(r: str) -> int:
    """ Return a Decimal Number by a Roman Number 'r' """
    if type(r) is not str:
        raise TypeError(f'Expect string, got {type(r)}')

    values = _values_for_each_letter(r)
    return sum(_map_representation(values))


def to_roman(d: int) -> str:
    """ Return a Roman Number by a Decimal Number 'd' """
    pass
