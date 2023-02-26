# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não teha sido informado corretamente.

def ficha(name='<Desconhecido>', gol=0):
    if name == '':
        name = '<Desconhecido>'
    print(f'O jogador {name} fez {gol} gol(s) no campeonato')


nome = str(input('Nome do Jogador: ')).strip( ).capitalize()
gols = input('Número de Gols: ')
if gols == '' or gols not in '1234567890':
    gols = 0
else:
    gols = int(gols)

ficha(nome, gols)
