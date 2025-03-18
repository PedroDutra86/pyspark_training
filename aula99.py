import sys

import aula99_package.modulo
from aula99_package.modulo import module_sum
from aula99_package import modulo
# Vou fazer a má pratica pois no módulo importado tem o __all__ para fins didaticos
# from aula99_package.modulo import *

# print(*sys.path, sep="\n")
# print(module_sum(1, 2))

# print(aula99_package.modulo.module_sum(3, 4))

# print(modulo.module_sum(6, 4))

# print(variable)
# print(new_variable) # Essa variavel está no módulo importado mas nao no __all__ por isso, inacessivel pelo *

# modulo.say_hello() # Todas as importações precisam ser no main, se não da esse erro aqui

from aula99_package import say_hello

say_hello()