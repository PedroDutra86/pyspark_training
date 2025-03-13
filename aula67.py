"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado
"""

def sum(x, y, z=None):
  if z is not None:
    print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')
  else:
    print(f'{x=} {y=} | x + y = {x + y}')

sum(1, 2, 5)
sum(4, 6)