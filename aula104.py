# Funções decoradores e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradores em outras funções
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def create_function(function):
  def inside(*args, **kwargs):
    print('Vou te decorar')
    for arg in args:
      is_string(arg)
    result = function(*args, **kwargs)
    print(f'O seu resoltado foi {result}')
    print('Ok, agora você foi decorada')
    return result
  return inside

@create_function
def reverse_string(string):
  print(f'{reverse_string.__name__}')
  return string[::-1]

def is_string(string):
  if not isinstance(string, str):
    raise TypeError(f'"{string} deve ser uma string"')


reversed_string = reverse_string('123')
print(reversed_string)