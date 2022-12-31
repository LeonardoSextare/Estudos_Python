# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = str(input('Digite um numero entre 0 e 9999: '))

num = num.replace(num, (4-len(num))*'0' + num)
print(num)
print(f'Numero Digitado: {num}\nUnidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')
