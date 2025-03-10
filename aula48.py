"""
Listas em Python
Tipo list -> Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis -> Índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'
lista = list()
# print(type(lista))
# lista = [24, 'Pedro Dutra']
# print(lista)
# lista[1] = 'Kathleen'
# print(lista)
lista.append(10)
print(lista)

lista.pop()
print(lista)

lista.append(50)
lista.append(60)
lista.append(70)
print(lista)
print(len(lista))

removed_value = lista.pop()
print(removed_value)
print(lista)

lista.insert(1, 40)
print(lista)

del lista[-1]
print(lista)

lista.clear()
print(lista)
print('--' * 10)
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)

print('--' * 10)

"""
Cuidados com dados mutáveis
= -> Copiando o valor (imutáveis)
= -> aponta para o mesmo valor na memória (mutáveis) 
"""

name = 'Pedro'
other_name = name
name = 'Kathleen'
print(name)
print(other_name)

lista_a = [10, 20]
lista_b = lista_a
lista_a[0] = 30

print(lista_b)