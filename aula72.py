"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar
Retorne se o número é par ou ímpar
"""

def multiply_values(*args):
  accumulator = 1
  for number in args:
    accumulator *= number
  return accumulator

def is_even_or_odd(number):
  if number % 2 == 0:
    return f'O número {number} é par'
  return f'O número {number} é ímpar'

multiply_five_numbers = multiply_values(1, 2, 3, 4, 5)
print(multiply_five_numbers)

even_number = is_even_or_odd(2)
print(even_number)

odd_number = is_even_or_odd(3)
print(odd_number)
