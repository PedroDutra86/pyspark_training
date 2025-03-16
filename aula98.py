import importlib

import aula98_m

print(aula98_m.variable)

for i in range(10):
  import aula98_m # Só vai executar uma vez porque é um singleton
  importlib.reload(aula98_m) # Aqui ele vai recarregar o codigo inteiro pois e uma biblioteca que faz o reload

print('fim')