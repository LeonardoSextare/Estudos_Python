#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um Número para converte-lo em outras bases: \n'))

escolha = str(input('Escolhe a base desejada: \n1 - Binario\n2 - Octal \n3 - Hexadecimal\n')).strip().lower()

if '1' in escolha or 'binario' in escolha or 'b' in escolha:
    print(f'O numero {num} em binario é: {bin(num)[2:]}')
elif '2' in escolha or 'octal' in escolha or 'o' in escolha:
    print(f'O numero {num} em octal é: {oct(num)[2:]}')
elif '3' in escolha or 'hexadecimal' in escolha or 'h' in escolha:
    print(f'O numero {num} em hexadecimal é: {hex(num)[2:]}')
else:
    print('Comando Invalido')