"""
Higher Order Functions
Funções de primeira classe
"""

def greeting(message, name):
  return f'{message}, {name}!'

def execute(function, *args):
  return function(*args)

print(execute(greeting, 'Good morning', 'Pedro'))
print(execute(greeting, 'Good evening', 'Kathleen'))