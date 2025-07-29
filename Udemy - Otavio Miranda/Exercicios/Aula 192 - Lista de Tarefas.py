# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
from time import sleep

tarefas = []
tarefas_desfeitas = []

lista_comandos = ("/listar", "/desfazer", "/refazer", "/sair")
while True:
    print("=== Lista de Tarefas ===")
    print("Comandos disponíveis:", *lista_comandos, sep="\n")
    input_usuario = input("Digite uma tarefa ou comando:")

    if input_usuario == lista_comandos[-1]:
        print("Saindo do programa.")
        break
    
    elif input_usuario == lista_comandos[0]:
        os.system("cls")
        print("=== Tarefas ===", *tarefas, sep="\n")
        input("Enter para continuar...")
        
    elif input_usuario == lista_comandos[1]:
        if len(tarefas) == 0:
            print("Não foi adicionado nenhuma tarefa.")
            continue
        
        tarefas_desfeitas.append(tarefas.pop())
        print(f"Tarefa '{tarefas_desfeitas[-1]}' desfeita.")
        
    elif input_usuario == lista_comandos[2]:
        if len(tarefas_desfeitas) == 0:
            print("Não há tarefas desfeitas.")
            continue
        
        tarefas.append(tarefas_desfeitas.pop())
        print(f"Tarefa '{tarefas_desfeitas[-1]}' adicionada.")
    else:
        tarefas.append(input_usuario)
        print(f"Tarefa '{input_usuario}' adicionada.")

    sleep(2)
    os.system("cls")
