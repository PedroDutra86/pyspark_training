"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condition = True
passed_if = None

if condition:
  passed_if = True
  print('Faça algo')
else:
  print('Não faça algo')  

print(passed_if, passed_if is None)
print(passed_if, passed_if is not None)