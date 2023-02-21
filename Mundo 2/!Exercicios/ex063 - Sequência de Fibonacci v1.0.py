# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 - 13 - 21 - 34

print('===== Sequencia de Fibonacci =====')
cont = int(0)
fibo = int()
n1 = 0
n2 = 1

elementos = int(input('Digite o número de elementos da Sequência de Fibonacci que deseja saber: \n'))
print('0 > 1 > ', end='')

while cont < elementos-2:
    fibo = (n2 + n1)
    print(f'{fibo} > ', end='')
    n1 = n2
    n2 = fibo
    
    cont += 1
