# Decoradores com parâmetros

def decorator_factory(*decorator_args):

  def function_factory(function):

    def nested(*args, **kwargs):
      print(f'Parâmetros do decorador {decorator_args}')
      result = function(*args, **kwargs)
      return result
    return nested
  return function_factory

decorator = decorator_factory(1, 2)

multiply = decorator(lambda x, y: x * y)
divide = decorator(lambda x, y: x / y)

ten_times_five = multiply(10, 5)
ten_divided_by_five = divide(10, 5)
print(ten_times_five)
print(ten_divided_by_five)