# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(termo,termo+(10*razao), razao):
    print( f'{c} >', end= ' ')
print('Fim')