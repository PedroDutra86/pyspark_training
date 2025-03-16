# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b, = b, a
# print(a, b)

person = {
  'name': 'Pedro',
  'surname': 'Dutra',
}

# a, b = person
# print(a, b)
# a, b = person.values()
# print(a, b)
# a, b = person.items()
# print(a, b)
# (a1, a2), (b1, b2)= person.items()
# print(a1, a2, b1, b2)

person_data = {
  'age': 24,
  'height': 1.8,
}

full_person = {**person, **person_data}

# print(full_person)

# args e kwargs
# args (já vimos)
# kwargs -> keyword arguments (argumentos nomeados)

def show_named_arguments(* args, **kwargs):
  for key, value in kwargs.items():
    print(key, value)

# show_named_arguments(nome='Pedro', 
# sobrenome='Dutra')

show_named_arguments(**full_person)

configs = {
  'arg1': 1,
  'arg2': 2,
  'arg3': 3,
  'arg4': 4,
}

show_named_arguments(**configs)