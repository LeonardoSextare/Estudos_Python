# Exercícios
# copy, sorted, produtos.sort
import copy

from dados import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
for i, produto in enumerate(novos_produtos):
    novos_produtos[i]["preco"] *= 1.10

print(*novos_produtos, sep='\n', end='\n\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda dicionario: dicionario["nome"], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n', end='\n\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda dicionario: dicionario["preco"])
print(*produtos_ordenados_por_preco, sep='\n', end='\n\n')