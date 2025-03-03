# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu): 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor

enter = input('[E]ntrar [S]air: ')
password = input('Senha: ')
verify_password = '12345'

if enter == 'E' and password == verify_password:
  print('Entrar')
else:
  print('Sair')

# Avaliação de curto circuito
print(True and False and True)