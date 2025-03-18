# Exercício - Unir listas # Crie uma função zipper (como o zipper de roupas) # O trabalho dessa função será unir duas # listas na ordem. # Use todos os valores da menor lista. # Ex.: # ['Salvador', 'Ubatuba', 'Belo Horizonte'] # ['BA', 'SP', 'MG', 'RJ'] # Resultado # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(first_list, second_list):
  maximum_range = min(len(first_list), len(second_list))
  return [
    (first_list[index], second_list[index]) for index in range(maximum_range)
  ]

cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_list = ['BA', 'SP', 'MG', 'RJ']
print(zipper(cities_list, states_list))

# -------- ou

print(list(zip(cities_list, states_list)))

# -------- ou

from itertools import zip_longest
print(list(zip_longest(cities_list, states_list)))