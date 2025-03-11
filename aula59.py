"""
Desempacotamento em chamadas de métodos e funções
"""

classrooms = [
  # 0        1           2
  ['Pedro', 'Kathleen', 'Tessa'], # 0
  # 0            1
  ['Marcilene', 'Edmar'], # 1
  # 0          1       2               
  ['Janaina', 'Igor', 'Maria Vitória',] # 2
]

print(*classrooms, sep='\n')

