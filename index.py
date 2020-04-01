"""
    Código de exemplo para uso do pacote de conversão:
        Romano -> Decimal
        Decimal -> Romano
"""

from roman import to_decimal

NUMEROS = (
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

if __name__ == '__main__':
    for decimal, romano in NUMEROS:
        converted = to_decimal(romano)

        print(f'{romano} => {converted}')
