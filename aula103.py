# Funções decoradores e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradores em outras funções

def create_function(function):
  def inside(*args, **kwargs):
    for arg in args:
      is_string(arg)
    result = function(*args, **kwargs)
    return result
  return inside

def reverse_string(string):
  return string[::-1]

def is_string(string):
  if not isinstance(string, str):
    raise TypeError(f'"{string} deve ser uma string"')

reverse_string_with_check = create_function(reverse_string)
reversed_string = reverse_string_with_check('123')
print(reversed_string)