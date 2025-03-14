"""
Closure e funções que retornam outras funções
"""

def create_greeting(greeting):
  def greet(name):
    return f'{greeting}, {name}!'
  return greet

say_good_morning = create_greeting('Good morning')
say_good_evening = create_greeting('Good evening')

for name in ['Pedro', 'Kathleen', 'Tessa']:
  print(say_good_morning(name))
  print(say_good_evening(name))
