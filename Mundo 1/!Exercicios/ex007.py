# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Digite o nome do aluno: \n')
nota1 = float(input('Digite a nota 1: \n'))
nota2 = float(input('Digite a nota 2: \n'))

print('A média do aluno: {} foi {}' .format(nome, (nota1+nota2)/2))