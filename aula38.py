"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

num_rows = 5
num_columns = 5

row = 1

while row <= num_rows:
  column = 1
  while column <= num_columns:
    print(f'{row=}, {column=}')
    column += 1
  row += 1

print('Acabou')