# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um numero decimal(numero com virgula): \n'))

print('O numero antes da virgula é {}'.format(math.trunc(num)))
print('O numero antes da virgula é {:.0f}'.format(num))
