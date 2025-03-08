"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

secret_word = 'perfume'
correct_letter = ''
attempts_number = 0

while True:
  typed_letter = input('Digite uma letra: ')
  attempts_number += 1

  if len(typed_letter) > 1:
    print('Digite apenas uma letra.')
    continue

  if typed_letter in secret_word:
    correct_letter += typed_letter

  formed_word = ''
  for secret_letter in secret_word:
    if secret_letter in correct_letter:
      formed_word += secret_letter
    else:
      formed_word += '*'

  print(f'Palavra formada {formed_word}')

  if formed_word == secret_word:
    os.system('clear')
    print('Você ganhou!')
    print(f'Tentativas: {attempts_number}')
    correct_letter = ''
    attempts_number = 0
    break