# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  P e d r o
# -5-4-3-2-1 
name = 'Pedro'
# print(name[2])
# print(name[-3])
print('dro' in name)
print('f' in name)
print('-' * 10)
print('dro' not in name)
print('f' not in name)

name = input('Digite seu nome: ')
search = input('Digite o que deseja encontrar: ')

if search in name:
  print(f'{search} está em {name}')
else:
  print(f'{search} não está em {name}')