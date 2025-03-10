import os

"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

shopping_cart = []

while True:
  list_options = input('''Selecione uma opção
[i]nserir [a]pagar [l]istar: 
''').lower()
  
  if list_options == 'i':
    os.system('clear')
    item_to_insert = input('Digite o que quer inserir no carrinho: ').capitalize()
    shopping_cart.append(item_to_insert)
    continue

  elif list_options == 'a':
    os.system('clear')
    item_index_to_delete = input('Digite o indice do item que você quer apagar: ')
    try:
      item_index_to_delete = int(item_index_to_delete)
      del shopping_cart[item_index_to_delete]
    except ValueError:
      print(f'"{item_index_to_delete}" não é um número')
    except IndexError:
      print(f'O índice "{item_index_to_delete}" não existe na lista')
    except Exception:
      print('Erro desconhecido')

  elif list_options == 'l':
    if shopping_cart:
      os.system('clear')
      for index, item in enumerate(shopping_cart):
        print(index, item)
        continue
    else:
      os.system('clear')
      print('Não há nada no carrinho')
      continue

  else:
    os.system('clear')
    print('Você digitou errado, quebrando o programa...')
    break