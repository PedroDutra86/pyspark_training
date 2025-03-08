"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

text = 'Pedro'
iterator = text.__iter__()

while True:
  try:
    print(iterator.__next__())
  except StopIteration:
    break