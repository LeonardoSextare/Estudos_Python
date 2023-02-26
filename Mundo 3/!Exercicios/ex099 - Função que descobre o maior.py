# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(n):
    if len(n) == 0:
        maior = 0
    else:
        maior = max(n)

    print(10*'=-', end='=\n')
    print('Analisando os valores passados...')
    for c in n:
        print(c, end=' ')
    print(f'Foram informados no total {len(n)} valores')
    print(f'O maior valor encontrado foi {maior}')
    print(10*'=-', end='=\n')


maior(2, 3, 6, 24, 75, 24)
maior(7, 4, 25, 7)
maior()
