#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('========== Gerador de Jogos ==========')
nJogos = int(input('Quantos jogos você quer gerar? '))
jogos = list()
jogosAux = list()
for c in range(0, nJogos):
    for x in range(0,6):
        nGerado = randint(1,60)
        while nGerado in jogosAux:
            nGerado = randint(1,60)
        jogosAux.append(nGerado)
    jogosAux.sort()
    jogos.append(jogosAux[:])
    jogosAux.clear()
    sleep(1)
    print(f'Jogo {c+1}:', jogos[c])
    
print('Boa Sorte!')