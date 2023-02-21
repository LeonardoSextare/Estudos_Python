#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número inteiro e veja seu fatorial:\n>>> '))
print(f'Calculando {num}! = {num}', end='')
resultado = num

while num != 1:
    num -= 1
    print(f' X {num}', end='')
    resultado *= num
    
print(f' = {resultado}')