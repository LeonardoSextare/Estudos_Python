from logico import *
from interface import *
from arquivos import *

inicializar(arquivo)

while True:
    mostrarMenu(menuPrincipal)
    linha()
    while True:
        escolha = leiaInt('Sua escolha:\n>> ')
        if validarLista(escolha, menuPrincipal):
            break
    sleep(0.5)

    mostrarMenu(menus[escolha])

    scriptMenu(escolha)
