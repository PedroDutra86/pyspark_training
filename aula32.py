"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
number = input('Digite um número: ')
try:
  number = int(number)
  is_even = number % 2 == 0
  if is_even:
    print(f'Número {number} é par')
  else:
    print(f'O número {number} é ímpar')
except ValueError:
  print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hour = input('Digite a hora: ')
try:
  hour = int(hour)
  if hour < 12:
    print('Bom dia')
  elif hour < 18:
    print('Boa tarde')
  elif hour < 24:
    print('Boa noite')
  else:
    print('Essa hora não existe')
except ValueError:
  print('Você não digitou a hora certa')

"""
Faça um programa que peça ao usuário o seu primeiro nome, Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
name = input('Digite seu nome: ')

try:
  if name.isalpha():
    if len(name) < 5:
      print('Seu nome é curto')
    elif len(name) < 7:
      print('Seu nome é normal')
    else:
      print('Seu nome é grande')
except ValueError:
  print('Seu nome está errado')