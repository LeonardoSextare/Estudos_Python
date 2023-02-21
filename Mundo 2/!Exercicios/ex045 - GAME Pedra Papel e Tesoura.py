# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random
print(f'===== Minigame: JOKENPO =====')

jogador = int(
    input('Escolha qual será sua jogada:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n'))

# Verifica se a jogada está correta
if jogador not in (0, 1, 2):
    print('Opção Invalida')
else:
    lista = ('Pedra', 'Papel', 'Tesoura')
    # Maquina escolhe uma jogada
    print('A maquina está pensando...')
    maquina = random.randint(0, 2)
    sleep(3)
    print(f'Você > {lista[jogador]} vs {lista[maquina]} < Maquina: ')

    # Resultado do Jogo
    if jogador == maquina:
        print('Empate!')

    elif jogador == 0:  # Pedra
        if maquina == 1:  # Papel
            print('A maquina venceu!')
        elif maquina == 2:  # Tesoura
            print('Você venceu!')

    elif jogador == 1:  # Papel
        if maquina == 0:  # Pedra
            print('Você venceu!')
        elif maquina == 2:  # Tesoura
            print('A maquina venceu!')

    else:  # Tesoura
        if maquina == 1:  # Papel
            print('Você venceu!')
        elif maquina == 0:  # Pedra
            print('A maquina venceu!')
