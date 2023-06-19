from termcolor import cprint, colored
from time import sleep
import os

menuPrincipal = [
    'Menu Principal',
    'Pessoas Cadastradas',
    'Novo Cadastro',
    'Sair do Sistema']

menus = [[menuPrincipal],
         ['Pessoas Cadastradas',],
         ['Novo Cadastro'],
         ['Encerrando o Programa...']]


def linha(tam=40):
    print('=' * tam)


def titulo(msg):
    linha()
    print(f'{msg:^40}')
    linha()


def mostrarMenu(items):
    os.system('cls')
    titulo(items[0])

    for c in range(1, len(items)):
        print(f'{c} - {items[c]}')


def aviso(msg, cor, tempo=0):
    cprint(msg, cor)
    sleep(tempo)
