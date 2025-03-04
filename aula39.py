"""
Iterando strings com while
"""

name = 'Pedro Dutra'

counter = 0
counter_limit = len(name)
new_name = ''

while counter < counter_limit:
  letter = name[counter]
  new_name += f'*{letter}'
  counter += 1

new_name += '*'
print(new_name)