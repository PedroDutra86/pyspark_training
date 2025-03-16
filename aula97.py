# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece as pastas onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

try:
  import sys
  # sys.path.append(r'C:\Users\conta\Documents\Estudos\Streamlit\src')
except:
  ...
import aula97_m
from aula97_m import variable_to_import_with_from
# import main

print(f'Este módulo se chama {__name__}')
# print(*sys.path, sep="\n")
print(aula97_m.module_variable)
print(variable_to_import_with_from)
soma = aula97_m.sum(4, 4)
print(soma)