# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorPeso = float(0)
menorPeso = float(1000)
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}° pessoa em Kg: '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'O menor peso foi de {menorPeso}Kg!\nO maior peso foi de {maiorPeso}Kg!')