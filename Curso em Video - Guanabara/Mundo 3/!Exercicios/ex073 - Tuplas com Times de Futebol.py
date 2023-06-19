#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG','Botafogo', 'Santos', 'Goiás', 'Brangatino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí','Juventude')
print('===== Informações do Brasileirão 2022 =====\n')

print('Lista de Times')
for c in (tabela):
    print(f'{c}')

print('\nPrimeiros 5 Colocados:')
for c in range(0,5):
    print(f'O {c+1}° colocado foi {tabela[c]}')

print('\nUltimos 5 Colocados:')
for c in range(19,14, -1):
    print(f'O {c+1}° foi {tabela[c]}')
    
print('\nTimes em Ordem Alfabética:')
for ordem in sorted(tabela):
    print(ordem, end=' ')
    
print('\n\nEm que posição está o Chapecoense:')
for c in range(0,len(tabela)):
    if tabela[c] in 'Chapecoense':
        print(f'Chapecoense está na {c+1}° posição')
        break
    elif c >= (len(tabela)-1):
        print('Chapecoense não foi encontrado na tabela')
        
        
print('\n\nEm que posição está o Palmeiras:')
for c in range(0,len(tabela)):
    if tabela[c] in 'Palmeiras':
        print(f'Palmeiras está na {c+1}° posição')
        break
    elif c >= (len(tabela)-1) :
        print('Palmeiras não foi encontrado na tabela')
