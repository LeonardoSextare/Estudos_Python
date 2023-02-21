# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('='*53)
    num = int(input('Digite um número inteiro para saber sua tabuada:\nNúmeros Negativos interropem o programa!\n>>> '))
    print('='*53)

    if num < 0:
        break
    
    for c in range(1,(11)):
        print(f'{num} X {c} = {num*c}')

print('Programa Encerrado!')