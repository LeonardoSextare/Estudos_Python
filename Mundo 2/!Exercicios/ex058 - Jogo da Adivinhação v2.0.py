#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint

c = float(0)
cont = int(0)

print('===== Minigame =====')
print('''Computador: Irei pensar em um número de 0 a 10, tente adivinhar!\nPensando...''')

sleep(randint(3,6))

escolha = randint(0,10)
resposta = int(-1)
print('Duvido você adivinhar o número que pensei!')

while resposta != escolha:
    resposta = int(input('Seu palpite: '))
    if resposta < escolha:
        print('Mais... Tente Novamente!')
    elif resposta > escolha:
        print('Menos... Tente Novamente!')
    cont += 1
    
print(f'Acertou! O número era {escolha}! E você precisou de {cont} palpites para acertar.')