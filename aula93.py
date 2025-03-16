# Try, except, else e finally

try:
  a = 18
  b = 0 # Aqui vai cair no NameError
  # print(b[0]) # Aqui ele cai no exception com TypeError, mas coloquei no Exception para fins didaticos
  # print('Linha 1'[1000]) # O erro aqui é IndexError
  c = a / b # Aqui vai cair no ZeroDivisionError
  print('Linha 2')
except ZeroDivisionError as e:
  print(e.__class__.__name__)
  print(e)
except NameError:
  print('Nome b não está definido')
except (TypeError, IndexError) as error:
  print('TypeError + IndexError')
  print(f'MSG: {error}')
  print(f'Nome: {error.__class__.__name__}')
except Exception:
  print('Erro desconhecido')

print('Continuando')