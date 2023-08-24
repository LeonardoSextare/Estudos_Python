"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


def somar_listas(*args):
    menor_indice = (len(lista) for lista in args)
    menor_indice = min(menor_indice)
    
    # listas_somadas = []
    # for i in range(menor_indice):
    #     soma = 0
    #     for lista in args:
    #         soma += lista[i]
    #     listas_somadas.append(soma)

    listas_somadas = [sum(list(zip(*args))[i]) for i in range(menor_indice)]
    return listas_somadas


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print(somar_listas(lista_a, lista_b))