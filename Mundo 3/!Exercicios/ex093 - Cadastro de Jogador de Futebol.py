# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome': '','gols':[],'total': 0}

jogador['nome'] = str(input('Digite o nome do jogador: '))
for c in range(0,int(input(f'Números de partidas do jogador {jogador["nome"]}:'))):
    jogador['gols'] += [int(input(f'Gols na partida {c+1}: '))]
    jogador['total'] += jogador['gols'][c]

print(jogador)
print(40*'=')
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, c in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1} ele fez {c} gols')
print(f'Total de {jogador["total"]} gols')