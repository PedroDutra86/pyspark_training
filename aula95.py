# raise -> lançando excelçoes (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def no_zero_allowed(d):
  if d == 0:
    raise ZeroDivisionError('Você está tentando dividir um número por 0')
  return True

def must_be_int_or_float(n):
  type_n = type(n)
  if not isinstance(n, (float, int)):
    raise TypeError(
      f'"{n}" deve ser int ou float. '
      f'"{type_n.__name__}" enviado'
    )
  return True

def divide(n, d):
  must_be_int_or_float(n)
  must_be_int_or_float(d)
  no_zero_allowed(d)
  return n / d

print(divide('8', 5))