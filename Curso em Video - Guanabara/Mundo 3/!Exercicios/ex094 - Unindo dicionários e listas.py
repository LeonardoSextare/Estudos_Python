#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

dicionario = {}
pessoas = []
media = 0
escolha = ' '
while escolha != 'n':
    dicionario['nome'] = str(input('Nome: '))
    
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: '))[0].lower()
        if dicionario['sexo'] in 'mf':
            break
        print('ERRO! Digite somente M ou F')
            
    dicionario['idade'] = int(input('Idade:'))
    media += dicionario['idade']
    
    pessoas.append(dicionario.copy())
    
    while True:
        escolha = str(input('Deseja cadastrar outra pessoa? [S/N]:'))[0].lower()
        if escolha in 'sn':
            break
        print('ERRO! Digite somente S ou N')

print(40*'=')
print(f'A) foram cadastradas no total: {len(pessoas)}')
print(f'B) a média de idade das pessoas cadastradas foi: {media/len(pessoas):.0f}')
print(f'C) mulheres cadastradas: ', end ='')
for c in pessoas:
    if c['sexo'] == 'f':
        print(f"[{c['nome']}] ", end='')
print(f'\nD) pessoas com idade acima da media:')
for c in pessoas:
    if c['idade'] > media/len(pessoas):
        for x, z in c.items():
            print(f'    {x} = {z}; ', end='')
