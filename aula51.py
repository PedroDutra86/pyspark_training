"""
Introdução ao desempacotamento
"""

*_, janaina, _ = ['Pedro', 'Kathleen', 'Tessa', 'Janaina', 'Marcilene']

*_, tessa, _, _ = ['Pedro', 'Kathleen', 'Tessa', 'Janaina', 'Marcilene']

*_, marcilene = ['Pedro', 'Kathleen', 'Tessa', 'Janaina', 'Marcilene']

pedro, *_ = ['Pedro', 'Kathleen', 'Tessa', 'Janaina', 'Marcilene']

print(janaina)
print(tessa)
print(marcilene)
print(pedro)