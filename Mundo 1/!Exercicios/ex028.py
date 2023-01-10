# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = int(input('Estou pensando em um numero de 0 a 5 tente adivinhar!'))
numr = random.randint(0,5)
if num == numr:
    print('Parabéns! Você acertou o numero!')
else:
    print(f'Você errou o numero :(\nO numero era: {numr}')
    