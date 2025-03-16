#Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem__iter__e__next__

lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
  print(n)

# Generator é algo MUUUITO mais leve do que uma lista por exemplo pois é algo que os valores não são armazenados, eles são entregues um por vez