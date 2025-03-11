"""
Lista de listas e seus índices
"""

classrooms = [
  # 0        1           2
  ['Pedro', 'Kathleen', 'Tessa'], # 0
  # 0            1
  ['Marcilene', 'Edmar'], # 1
  # 0          1       2               
  ['Janaina', 'Igor', 'Maria Vitória',] # 2
]

print(classrooms[0][2])

for index, classroom in enumerate(classrooms):
  for student in classroom:
    print(f'sala {index}, estudante {student}')