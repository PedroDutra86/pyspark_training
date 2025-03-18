# Exercício -> Adiando execução de funções

def sum(x, y):
  return x + y

def multiply(x, y):
  return x * y

def execute(function, x):
  def delay_function(y):
    return function(x, y)
  return delay_function

sum_with_five = execute(sum, 5)
multiply_by_ten = execute(multiply, 10)

print(sum_with_five(2))
print(multiply_by_ten(10))