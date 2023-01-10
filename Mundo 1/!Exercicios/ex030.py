#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um numero e saiba se é Par ou Impar: \n'))

if num%2 == 0:
    print('O numero é Par!')
else:
    print('O numero é Impar!')