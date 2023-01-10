# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))
n3 = float(input('Terceiro numero: '))
aux = float

if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux

if n3 > n1:
    aux = n3
    n3 = n1
    n1 = aux

if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux

print(f'Maior Numero: {n1}\nMenor Numero: {n3}')
