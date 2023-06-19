# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = int(0)
while True:
    num = int(input('Digite um número inteiro para adicionar a lista:\nDigite "999" para ver o resultado da lista.\n>>> '))
    if num == 999:
        break
    cont += 1
    soma += num
    
print(f'Você digitou {cont} números e a soma deles é igual a {soma}')
