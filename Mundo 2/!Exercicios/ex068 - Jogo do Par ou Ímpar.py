# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

venceu = 0

while True:
    print(f'{" Par ou Impar ":=^50}')
    
    while True: #Validador da Jogada
        jogador = int(input('Digite um número inteiro de 0 a 10: '))
        if jogador >= 0 and jogador <= 10:
            break
        else:
            print('Número Invalido! Tente novamente.')
    
    while True: #Validador da Escolha
        escolha = str(input('Você quer Impar ou Par?[I/P]: ')).lower()[0]
        if escolha == 'i' or escolha == 'p':
            break
        else:
            print('Jogada Invalida! Tente novamente.')
    
    #Maquina escolhe o número dela.
    maquina = randint(0,10)
    print(f'A maquina escolheu: {maquina}')
    
    #Dá o resultado do Jogo
    if (maquina+jogador)%2 == 0:
        print(f'{jogador} + {maquina} = {jogador+maquina} que é PAR. Você Venceu!')
        venceu += 1
    else:
        print(f'{jogador} + {maquina} = {jogador+maquina} que é Impar. Você Perdeu!')
        break
    
print(f'Fim de Jogo! Você venceu a maquina um total de {venceu} vezes!')
    
    
    
    
    
    
            
        
    
