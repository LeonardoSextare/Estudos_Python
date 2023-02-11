# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from time import localtime

print('Calculadora de Maioridade')

maiorIdade = int(0)
menorIdade = int(0)

for c in range(1, 9):
    idade = int(input(f'Qual o ano de nascimento da {c}° pessoa?'))
    if localtime().tm_year - idade >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f'O número de pessoas menores de idade foram de {menorIdade}!')
print(f'O número de pessoas maiores de idade foram de {maiorIdade}!')

