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
    if lista:
        return True
        
    print(f'Nada a {comando.lower()}')
    return None


def executar_comando(mensagem: str):
    if mensagem not in comandos:
        # Adiciona a Lista
        tarefas.append(mensagem)
        print(*tarefas, sep='\n')
        return
    
    # Listar
    if mensagem == comandos[0]:
        print(*tarefas, sep='\n') if checar_lista_vazia(tarefas, comandos[0]) else None

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

    


while True:
    print('=-= Lista de Tarefas =-=')
    print('Comandos:', *comandos)
    escolha = input('Digite uma tarefa ou comando:\n>> ').strip().capitalize()
    executar_comando(escolha)
    print()
