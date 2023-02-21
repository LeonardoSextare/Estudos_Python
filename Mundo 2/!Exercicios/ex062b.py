# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
from os import system
print('===== Calculadora de PA =====')
termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
termoaux = termo
historico = str('')
escolha = str('')


while escolha == '':
    system('cls')
    print(f'Primeiro Termo: {termo}\nRazão da PA: {razao}')
    
    print(historico, end='')
    historico += (f'{termoaux} > ')
    
    termoaux += razao
    
    escolha = str(input('\nDigite Enter para mostrar o proximo termo ou digite qualquer coisa para sair do programa'))
    
print('Fim do Programa')