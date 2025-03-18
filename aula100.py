import copy

from dados import products

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
new_products = [
  {**product, 'price': f'{product['price'] * 1.1:.2f}'}
  for product in copy.deepcopy(products)
]

# print(*products, sep="\n")
# print()
# print(*new_products, sep="\n")


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

products_sorted_by_name = sorted(
  copy.deepcopy(products),
  key = lambda product: product['name'],
  reverse=True
)

# print(*products, sep="\n")
# print()
# print(*products_sorted_by_name, sep="\n")

# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

products_sorted_by_price = sorted(
  copy.deepcopy(products),
  key = lambda product: product['price'],
)

print(*products, sep="\n")
print()
print(*new_products, sep="\n")
print()
print(*products_sorted_by_name, sep="\n")
print()
print(*products_sorted_by_price, sep="\n")