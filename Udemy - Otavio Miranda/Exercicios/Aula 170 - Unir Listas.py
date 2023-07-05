# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
# terceira_lista = [1, 2, 3, 4]


def zipper(*args):
    print('Argumentos:', args)
    menor_lista = args[0]
    for i in range(len(args)):
        if len(args[i]) < len(menor_lista):
            menor_lista = args[i]
            print('\nMenor Lista:', menor_lista)


    lista_unida = []
    for i in range(len(menor_lista)):
        lista_temp = []
        for lista in [*args]:
            lista_temp.append(lista[i])
        lista_unida.append(tuple(lista_temp))
    return lista_unida


# print('\n\n',zipper(cidades, estados, terceira_lista))
print('\n\n',zipper(cidades, estados))
