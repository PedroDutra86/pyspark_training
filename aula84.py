# List comprehension em Python
# List comprehension é uma forma ráppida para criar listas a partir de iteráveis

# lista = []
# for number in range(10):
#   lista.append(number)
# print(lista)
import pprint

def p(v):
  pprint.pprint(v, sort_dicts=False, width=40)

lista = [numero * 2 for numero in range (10)]
# print(lista)

# Mapeamento de dados em list comprehension
products = [
  {'name': 'p1', 'price': 20},
  {'name': 'p2', 'price': 10},
  {'name': 'p3', 'price': 30},
]

new_products = [
  {**product, 'price': product['price'] * 1.05} 
  if product['price'] > 20 else product 
  for product in products
  if product['price'] > 10
  ]

p(new_products)



