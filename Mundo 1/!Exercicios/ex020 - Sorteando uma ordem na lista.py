# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A sequencia de alunos são: \n1° - {}\n2° - {}\n3° - {}\n4° - {}' .format(alunos[0],alunos[1],alunos[2],alunos[3]))
