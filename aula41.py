"""while/else"""
string = 'Qualquer valor'

i = 0
while i < len(string):
  letter = string[i]

  print(letter)
  i += 1
  if i == 7:
    break
else:
  print ('O else foi executado')
print('Fora do while.')