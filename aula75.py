"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""

def create_multiplier(multiplier):
  def number_to_multiply(multiplicand):
    return multiplier * multiplicand
  return number_to_multiply

double_value = create_multiplier(2)
triple_value = create_multiplier(3)
quadruple_value = create_multiplier(4)

print(double_value(3))
print(triple_value(3))
print(quadruple_value(3))