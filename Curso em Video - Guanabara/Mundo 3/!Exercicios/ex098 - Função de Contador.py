# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    #print(15 * '=-', end='=\n')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo *= -1
            fim -= 1
        elif passo < 0:
            fim -= 1
    elif inicio < fim:
        if passo > 0:
            fim += 1
        elif passo < 0:
            print('Não é possivel fazer está contagem!')
            
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM')
    print(15 * '=-', end='=\n')


contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez: ')
ini = int(input('Inicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
