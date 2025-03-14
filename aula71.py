"""
args -> Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembrete de desempacotamento

# x, y, *_ = 1, 2, 3, 4, 5, 6
# print(x, y, _)

def sum(*args):
  accumulator = 0
  for number in args:
    accumulator += number
  return accumulator

first_sum = sum(1, 2, 3, 4)
print(first_sum)

numbers = 1, 2, 3, 4, 5, 6
second_sum = sum(*numbers)
print(second_sum)

