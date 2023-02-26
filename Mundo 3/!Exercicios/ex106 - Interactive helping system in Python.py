# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from colorama import init, Back, Fore, Style
init()

def ajuda(nome):
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + 20*'=-'+f'\n{f"Acessando o Comando {nome}":^40}\n' + 20*'=-' + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + Style.BRIGHT)
    help(nome)
    print(Style.RESET_ALL)


while True:
    
    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 10*'=-'+f'\n{"Sistema de Ajuda":^20}\n' + 10*'=-' + Style.RESET_ALL)
    print()
    escolha = str(input('Digite o nome de uma biblioteca ou função para receber ajuda:\n>>> ')).strip().lower()
    if escolha == 'fim':
        print('Obrigado por utilizar nossos serviços. Até Logo!')
        break
    
    ajuda(escolha)