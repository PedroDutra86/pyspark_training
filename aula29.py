"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

number = input('Vou dobrar o número que você digitar: ')

try:
  float_number = float(number)
  print(f'O dobro de {number} é {float_number * 2}')
except:
  print('Isso não é um número')