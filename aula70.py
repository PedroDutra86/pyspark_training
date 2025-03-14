"""
Retorno de valores das funções (return)
"""

def sum(x, y):
  if x > 10:
    return [10, 20]
  return x + y

first_sum = sum(5, 5)
second_sum = sum(6, 6)
third_sum = sum(15, 5)
print(first_sum)
print(second_sum)
print(third_sum)