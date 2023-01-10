# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior, Não existe valor maior, os dois são iguais

num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num > num2:
    print(f'O numero {num} é maior que {num2}')
elif num < num2:
    print(f'O numero {num} é menor que {num2}')
else:
    print(f'O numero {num} é igual a {num2}')
