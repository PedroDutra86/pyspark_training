"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""

def sum(x, y):
  print(f'{x=} {y=} | x + y = {x + y}')

sum(2, 3)
sum(3, 2)
sum(y=3, x=2)