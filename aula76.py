"""Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

person = {
    'name': 'Pedro Paulo',
    'surname': 'Dutra',
    'age': 18,
    'height': 1.8,
    'address': [
        {'street': 'Rua Dep. Altair de Oliveira Lima', 'number': 264},
        {'street': 'Vila Rica', 'number': 2}
    ],
    # 'birthday': 2001
}
# print(person['name'], end=' ')
# print(person['surname'])

# Manipulando chaves e valores em dicionários

person['spouse'] = 'Kathleen'
# print(person['spouse'])
person['daughter'] = 'Tessa'
del person['spouse']
# print(person)

if person.get('spouse') is not None:
    ...
    # print('Existe')
else:
    person['spouse'] = 'Kathleen'
    # print('Não existe')

# print(person)

"""
Métodos úteis dos dicionários em Python
len -> quantas chaves
keys -> iterável com as chaves
values -> iterável com os valores
items -> iterável com chaves e valores
setdefault -> adiciona valor se a chave não existe
copy -> renorna uma cópia rasa (shallow copy)
get -> obtém uma chave
pop -> Apaga um item com a chave especificadda (del)
popitem -> Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

# print(len(person))
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.setdefault('birthday', 'Não tem'))
# print(person.get('name')) # -> Se não tivesse a chave name no dict, a função get retornaria None
# name = person.pop('name');print(name);print(person)
# last_key = person.popitem();print(last_key);print(person) # Não aceita que seja colocado atributos, retorna um dicionario com a chave e o valor deletado
# person.update({
    # 'job': 'Mobi'
# });print(person) # Update atualiza o dicionario se houver a chave, se nao houver ele cria, pode também receber iteráveis que sejam separados com dois valores como por exemplo (('name', 'Pedro), ('age': 30))

# for key, value in person.items():
#     print(f'chave: {key}, valor: {value}')



# Shallow copy and Deep copy

second_person = person.copy() # Isso é uma shallow copy, pois quando falamos de valores mutáveis, apenas colocar que uma variavel recebe outra não faz a cópia, apenas referencia o mesmo valor na memória, e caso eu mudasse qualquer uma das variaveis, afetaria a outra, diferente com imutáveis, que ao atribuir faz a cópia

# Importante, a shallow copy não entra em subníveis, então mesmo que faça uma cópia e dentro do valor mutável você tiver outro valor mutável, o Python vai fazer como faz quando colocamos o sinal de atribuição, apenas uma referência a esse dado interno

# Para fazer uma deep copy, precisamos de:

import copy

second_person = copy.deepcopy(person)