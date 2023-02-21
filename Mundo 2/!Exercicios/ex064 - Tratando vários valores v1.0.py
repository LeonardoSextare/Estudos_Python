#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('===== Somador de Números =====')
cont = lista = num = int(0)
while num != 999:
    num = int(input('Digite um número inteiro para adicionar a lista de soma\nDigite "999" para somar todos os números digitados\n>>>'))
    if num != 999:
        lista += num
        cont += 1
print(f'A quantidade de números digitados foram {cont} e a soma deles é igual a: {lista}')