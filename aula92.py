# Yield from

def gen1():
  print('Começou Gen1')
  yield 1
  yield 2
  yield 3
  print('Acabou Gen1')

def gen3():
  print('Começou Gen3')
  yield 10
  yield 20
  yield 30
  print('Acabou Gen3')

def gen2(gen):
  print('Começou Gen2')
  yield from gen()
  yield 4
  yield 5
  yield 6
  print('Acabou Gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)

for number in g1:
  print(number)

for number in g2:
  print(number)