saved_password = '123456'
entered_password = ''
repetitions = 0

while saved_password != entered_password:
  entered_password = input(f'Sua senha ({repetitions}x): ')

  repetitions += 1
  if repetitions == 3:
    print('Bloqueado')
    break

print(repetitions)

text = 'Python'
new_text = ''

for letter in text:
  new_text += f'*{letter}'
  print(letter)

print(new_text + '*')