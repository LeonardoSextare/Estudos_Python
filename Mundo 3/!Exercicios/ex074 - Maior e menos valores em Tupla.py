#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

valores = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'O números gerados são: {valores}')

print(f'Maior valor: {sorted(valores)[4]}')

print(f'Menor valor: {sorted(valores)[0]}')

print(f'Maior valor: {max(valores)}')

print(f'Menor valor: {min(valores)}')