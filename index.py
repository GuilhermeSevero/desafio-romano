"""
    Código de exemplo para uso do pacote de conversão:
        Romano -> Decimal
        Decimal -> Romano
"""

from roman import to_decimal, to_roman


NUMBERS = (
    (1, 'I'),
    (2, 'II'),
    (4, 'IV'),
    (5, 'V'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (138, 'CXXXVIII'),
    (170, 'CLXX'),
    (215, 'CCXV'),
    (390, 'CCCXC'),
    (483, 'CDLXXXIII')
)


def _print_roman_to_decimal():
    print('--- Romano para Decimal ---')
    for decimal, roman in NUMBERS:
        converted = to_decimal(roman)

        print(f'{roman} => {converted}')


def _print_decimal_to_roman():
    print('--- Decimal para Romano ---')
    for decimal, roman in NUMBERS:
        converted = to_roman(decimal)

        print(f'{decimal} => {converted}')


if __name__ == '__main__':
    _print_roman_to_decimal()
    print('\n')
    _print_decimal_to_roman()
