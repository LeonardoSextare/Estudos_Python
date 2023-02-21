# Crie um programa que leia dois valores e mostre um menu na tela
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('===== Calculadora =====')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

while True:
    print('===== Calculadora =====')
    escolha = int(input('''\nEscolha qual operação deseja realizar com números escolhidos:
    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos Números
    5 - Sair do Programa\n'''))

    if escolha == 1:
        print(f'A soma de: {n1} + {n2} é {n1+n2}')
        sleep(3)
        
    elif escolha == 2:
        print(f'O resultado de {n1} X {n2} é {n1*n2}')
        sleep(3)
        
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é menor que {n1}')
        else:
            print(f'{n1} é igual a {n2}')
        sleep(3)
        
    elif escolha == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))  
        
    elif escolha == 5:
        print('Encerrando o programa...')
        exit()
        
    