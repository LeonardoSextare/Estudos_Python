# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

lista = []


def sorteia(n):
    print('Sorteando 5 valores na lista: ', end='', flush=True)
    for c in range(5):
        n.append(randint(0, 10))
        sleep(0.5)
        print(n[c], end=' ', flush=True)
    print()


def somaPar(n):
    """
    Teste 123
    """
    s = 0
    for c in n:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de: {n}...')
    sleep(1)
    print(f'Resultado: {s}')


sorteia(lista)

somaPar(lista)

help(somaPar)