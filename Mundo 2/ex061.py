# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('===== Calculadora de PA =====')
termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
cont = int(0)
while cont <= 9:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('Fim')