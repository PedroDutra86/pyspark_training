def execute(function, *args):
  return function(*args)

# def sum(x, y):
#   return x + y

# def create_multiplier(multiplier):
#   def multiply(number):
#     return number * multiplier
#   return multiply

print(execute(lambda x, y: x + y, 4, 5))

double_value = execute(lambda m: lambda n: n * m, 2)
print(double_value(4))

print(execute(lambda *args: sum(args), 4, 5, 2, 3))