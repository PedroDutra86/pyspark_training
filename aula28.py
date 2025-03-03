"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
  Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
  exiba: "Desculpe, você deixou campos vazios."
"""

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

if name and age:
  print(f'Seu nome é {name}')
  print(f'Seu nome invertido é {name[::-1]}')
  if ' ' in name:
    print('Seu nome tem espaços')
  else:
    print('Seu nome não tem espaços')
  print(f'Seu nome tem {len(name)} letras')
  print(f'A primeira letra do seu nome é {name[0]}')
  print(f'A última letra do seu nome é {name[-1]}')
else:
  print('Desculpe, você deixou campos vazios')