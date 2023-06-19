# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint

jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6),
             }

print('Sorteando valores...')
for n, r in jogadores.items():
    sleep(1)
    print(f'{n} tirou {r} no dado.')

rank = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print(40*'=' + '\n   == Ranking do Jogadores ==')
for i in range(0,len(rank)):
    sleep(1)
    print(f'    {i+1}° lugar - {rank[i][0]} com {rank[i][1]}')

