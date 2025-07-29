import os
from time import sleep
import json
from pathlib import Path


CAMINHO_ATUAL = Path(__file__).parent

def limpar_tela():
    os.system("cls")


def listar(tarefas):
    print("=== Tarefas ===", *tarefas, sep="\n")
    input("Enter para continuar...")


def adicionar(tarefa, tarefas):
    if tarefa in tarefas:
        print("Tarefa já foi adicionada.")
        return

    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada a lista.")


def desfazer(tarefas, tarefas_desfeitas):
    if not tarefas:
        print("Não existem tarefas na lista.")
        return

    tarefas_desfeitas.append(tarefas.pop())
    print(f"Tarefa '{tarefas_desfeitas[-1]}' desfeita.")


def refazer(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas:
        print("Não há tarefas desfeitas.")
        return

    tarefas.append(tarefas_desfeitas.pop())
    print(f"Tarefa '{tarefas[-1]}' adicionada a lista.")


def carregar_json(caminho_arquivo=f"{CAMINHO_ATUAL}\\tarefas.json"):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            tarefas_dict = json.load(arquivo)
            return tarefas_dict

    except FileNotFoundError as e:
        return {"tarefas": [], "tarefas_desfeitas": []}


def salvar_json(tarefas_dict, caminho_arquivo=f"{CAMINHO_ATUAL}\\tarefas.json"):
    with open(caminho_arquivo, "w+") as arquivo:
        json.dump(tarefas_dict, arquivo)


def sair(tarefas):
    print("Salvando dados...")
    salvar_json(tarefas)
    exit()


tarefas_dict = carregar_json()
comandos = {
    "/listar": lambda: listar(tarefas_dict["tarefas"]),
    "/desfazer": lambda: desfazer(*tarefas_dict.values()),
    "/refazer": lambda: refazer(*tarefas_dict.values()),
    "/sair": lambda: sair(tarefas_dict),
}
func_adicionar = lambda: adicionar(input_usuario, tarefas_dict["tarefas"])

while True:
    print("=== Lista de Tarefas ===")
    print("Comandos disponíveis:", *comandos.keys(), sep="\n")
    input_usuario = input("Digite uma tarefa ou comando:")

    comando = comandos.get(input_usuario, func_adicionar)
    comando()

    sleep(2)
    limpar_tela()
