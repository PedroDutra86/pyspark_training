# Exemplo de uso dos sets

letters = set()

while True:
  letter = input('Digite: ')
  letters.add(letter.lower())

  if 'l' in letters:
    print('Parabéns!')
    break

  print(letters)
