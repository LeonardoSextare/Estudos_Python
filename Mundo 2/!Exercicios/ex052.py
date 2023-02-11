# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero inteiro: '))

for c in range(2, num,):
    if num % c == 0:
        print(f'O numero {num} não é primo pois é divisivel por {c}')
        exit()

print(f'O numero {num} é primo!')

#+- certo