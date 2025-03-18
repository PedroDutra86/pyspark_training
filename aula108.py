# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

print('C1 tem __iter__?', hasattr(c1, '__iter__'))
print('C1 tem __next__?', hasattr(c1, '__next__'))

print()

print('R1 tem __iter__?', hasattr(r1, '__iter__'))
print('R1 tem __next__?', hasattr(r1, '__next__'))

print('count')
for i in c1:
  if i >= 100:
    break
  print(i)

print()

print('range')
for i in r1:
  print(i)