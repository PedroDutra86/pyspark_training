# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


first_set = set()  # vazio
first_set = {'Pedro', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

first_set.add('Kathleen')
print(first_set)
first_set.update(('Tessa',)) # Se for passado somente o valor ele vai iterar sobre o valor
print(first_set)
first_set.discard(1) # Como não existe indices, quando utilizar o discard, você colocara o proprio valor
print(first_set)
first_set.clear()
print(first_set)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

first_set = {1, 2, 3}
second_set = {2, 3, 4}
third_set = first_set | second_set
fourth_set = first_set & second_set
fifth_set = first_set - second_set
sixth_set = first_set ^ second_set

print(first_set)
print(second_set)
print(third_set)
print(fourth_set)
print(fifth_set)
print(sixth_set)
