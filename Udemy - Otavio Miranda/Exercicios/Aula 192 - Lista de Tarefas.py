# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


comandos = ('Listar', 'Desfazer', 'Refazer', 'Clear')
tarefas = []
excluido = []


def checar_lista_vazia(lista: list, comando: str):
    if len(lista) == 0:
        print(f'Nada a {comando.lower()}')
        return None
    else:
        return True


def checar_comando(mensagem: str):
    if mensagem in comandos:
        # Listar
        if mensagem == comandos[0]:
            if checar_lista_vazia(tarefas, comandos[0]):
                print(*tarefas, sep='\n')

        # Desfazer
        elif mensagem == comandos[1]:
            if checar_lista_vazia(tarefas, comandos[1]):
                excluido.append(tarefas.pop())
                print(*tarefas, sep='\n')

        # Refazer
        elif mensagem == comandos[2]:
            if checar_lista_vazia(excluido, comandos[2]):
                tarefas.append(excluido.pop())
                print(*tarefas, sep='\n')

        # Clear
        elif mensagem == comandos[3]:
            os.system('cls')

    # Adiciona a Lista
    else:
        tarefas.append(mensagem)
        print(*tarefas, sep='\n')


while True:
    print('=-= Lista de Tarefas =-=')
    print('Comandos:', *comandos)
    escolha = input('Digite uma tarefa ou comando:\n>> ').strip().capitalize()
    checar_comando(escolha)
    print()
