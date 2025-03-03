"""
Interpolação básica de strings
s- string
d e i - int
f - float
x e X - Hexadecimal
"""

name = 'Pedro'
price = 1000.95897642
variable = '%s, o preço total foi R$%.2f' % (name, price)
print(variable)

print('O hexadecimal de %d é %06X' % (30, 30))