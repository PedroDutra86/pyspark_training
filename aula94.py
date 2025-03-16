# try, except, else e finally

try:
  print('Abri o arquivo')
  # print(8/0)
except ZeroDivisionError:
  print('Dividiu Zero')
else:
  print('Não deu erro')
finally:
  print('Fechou o arquivo')