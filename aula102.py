# Variáveis livres _ nonlocal (locals, globals)

# print(globals())

def outside(x):
  a = x
  def inside():
    # print(locals())
    print(inside.__code__.co_freevars)
    return a
  return inside

inside = outside(10)
inside_1 = outside(20)

print(inside())
print(inside_1())

def concatenate(initial_string):
  final_value = initial_string

  def inside(value_to_concatenate):
    nonlocal final_value
    final_value += value_to_concatenate
    return final_value
  return inside

c = concatenate('a')
print(c('b'))
print(c('c'))
print(c('d'))