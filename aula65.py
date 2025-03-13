"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
Por padrão, funções em Python retornam None (nada)
"""
def imprimir(a, b, c):
  print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def greeting(name='unnamed'):
  print(f'Olá {name}!')

greeting('Pedro Dutra')
greeting('Kathleen Couto')
greeting()