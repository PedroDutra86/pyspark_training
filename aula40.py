""" Calculadora com while """

while True:
  first_operand = int(input('Digite um número: '))
  second_operand = int(input('Digite o segundo número: '))
  operator = input(f'Escolha o operador para realizar o calculo \
  \n{first_operand} [+] {second_operand}\
  \n{first_operand} [-] {second_operand}\
  \n{first_operand} [*] {second_operand}\
  \n{first_operand} [/] {second_operand}\nR: ')
  if operator == '+':
    print(f'{first_operand + second_operand}')
  elif operator == '-':
    print(f'{first_operand - second_operand}')
  elif operator == '*':
    print(f'{first_operand * second_operand}')
  elif operator == '/':
    print(f'{first_operand / second_operand}')
  else:
    print('Você não digitou nada, quebrando o programa')
    break
  continue_prompt = input('Você quer sair do programa? S/N').upper()
  if continue_prompt == 'S':
    break