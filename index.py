"""
    Código de exemplo para uso do pacote de conversão:
        Romano -> Decimal
        Decimal -> Romano
"""

import roman


if __name__ == '__main__':
    print('--- Romano para Decimal ---')

    value = 'CMXCVIII'
    converted = roman.to_decimal(value)

    print(f'{value} -> {converted}')

    print('\n')

    print('--- Decimal para Romano ---')

    value = 998
    converted = roman.to_roman(value)

    print(f'{value} -> {converted}')
