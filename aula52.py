"""
Tiplo tupla -> Uma lista imutável
"""

names = ('Pedro', 'Kathleen', 'Tessa')
print(names, type(names))

# names = list(names)
# print(names, type(names))

#Metodos
numbers = (1, 2, 3, 4, 2, 2, 1)
print(numbers.count(2))
print(numbers.index(2))