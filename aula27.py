"""
Fatiamento de strings
  012345678
  Olá mundo
- 987654321 
Fatiamento [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da str
"""
variable = 'Olá mundo'
print(variable[4:])
print(variable[:5])
print(variable[-8:-2])
print(variable[0::2])
print(variable[:8:2])
print(variable[::-1])

print(len(variable))
print(variable[0:len(variable):1])