# dir, hasattr e getattr em Python
string = 'Pedro'
metodo = 'upper1'


if hasattr(string, metodo):
  print('Existe upper')
  print(getattr(string, metodo)())
else:
  print(f'Não existe o método {metodo}')


string_items = [
  method 
  for method in dir(string)
]

# for method in string_items:
#   print(method)