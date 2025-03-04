"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

counter = 0

while counter <= 10:
  counter += 1
  if 4 <= counter <= 8:
    print(f'Não vou mostrar o {counter}')
    continue
  print(counter)

print('Acabou')