# Ordem dos decoradores

def decorator_parameters(name):
  def decorator(function):
    print(f'Decorador {name}')

    def your_new_function(*args, **kwargs):
      result = function(*args, **kwargs)
      final = f'{result} {name}'
      return final
    return your_new_function
  return decorator

@decorator_parameters(name='terceiro')
@decorator_parameters(name='segundo')
@decorator_parameters(name='primeiro')
def sum(x, y):
  return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)