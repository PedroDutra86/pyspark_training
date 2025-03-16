# Dictionary Comprehension e Set Comprehension

product = {
  'name': 'Caneta Azul',
  'price': 2.5,
  'category': 'Escritório',
}

new_dc = {
  key: value.upper() 
  if isinstance(value, str) else value
  for key, value
  in product.items()
  if key != 'category'
}

print(new_dc)

set_comprehension = {
  i for i in range(10)
}
print(set_comprehension)