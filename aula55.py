"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

first_number = 0.1
second_number = 0.7
third_number = first_number + second_number
print(third_number)
print(f'{third_number:.2f}')
print(round(third_number, 2))

first_number = decimal.Decimal('0.1')
second_number = decimal.Decimal('0.7')
third_number = first_number + second_number
print(third_number)