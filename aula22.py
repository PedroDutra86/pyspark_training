# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu): 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor

enter = input('[E]ntrar [S]air: ')
password = input('Senha: ')
verify_password = '12345'

if (enter == 'E' or enter == 'e') and password == verify_password:
  print('Entrar')
else:
  print('Sair')

# Avaliação de curto circuito
password = input('Senha: ') or 'Sem senha'
print(password)