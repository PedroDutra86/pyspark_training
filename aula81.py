# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'name': 'Pedro', 'surname': 'Dutra'},
    {'name': 'Kathleen', 'surname': 'Couto'},
    {'name': 'Tessa', 'surname': 'Vizani'},
    {'name': 'Janaina', 'surname': 'Granja'},
    {'name': 'Maria Vitória', 'surname': 'Gonçalves'},
]

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)


def show_list(list):
  for item in list:
    print(item)
  print()

first_list = sorted(lista, key=lambda item: item['name'])
second_list = sorted(lista, key=lambda item: item['surname'])

show_list(first_list)
show_list(second_list)

# Sort retorna a propria função organizada
# Sorted retorna outra função e faz uma shallow copy
