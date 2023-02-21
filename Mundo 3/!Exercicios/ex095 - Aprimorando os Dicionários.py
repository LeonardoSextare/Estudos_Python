# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []
jogador = {'nome': '','gols':[],'total': 0}

escolha = ' '
while escolha != 'n':
    jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
    for c in range(0,int(input(f'Números de partidas do jogador {jogador["nome"]}:'))):
        jogador['gols'] += [int(input(f'Gols na partida {c+1}: '))]
        jogador['total'] += jogador['gols'][c]
    
    while True:
        escolha = ' '
        escolha = str(input('Deseja cadastrar outro jogador? [S/N]'))
        if escolha in 'sn':
            break
        print('ERRO! Digite somente [S/N]!')
        
    time.append(jogador.copy())
    jogador = {'nome': '','gols':[],'total': 0}
    
print(40*'=' + '\ncod  nome          gols           total\n' + 40*'-')
for i, c in enumerate(time):
    print(f'{i:>3} {c["nome"]:<14} {str(c["gols"]):<15} {c["total"]}')

while escolha != 999:
    while True:
        print(40*'=')
        escolha = int(input('Deseja mostrar os dados de qual jogador?[999 - Encerra]'))
        if escolha == 999 or escolha < len(time):
            break
        print(f'ERRO! Não existe jogador com o codigo {escolha}!')
        
    print(40*'=')
    print(f'O Jogador {time[escolha]["nome"]} jogou {len(time[escolha]["gols"])} partidas')
    for i, c in enumerate(time[escolha]['gols']):
        print(f'    => Na partida {i+1} ele fez {c} gols')
    print(f'Total de {time[escolha]["total"]} gols')
    