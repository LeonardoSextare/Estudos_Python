#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
listaAux = []
maior = menor = 0
escolha = 's'
while escolha != 'n':
    listaAux.append(str(input('Digite o nome da pessoa: ').capitalize()))
    listaAux.append(float(input('Digite o peso da pessoa em Kg: ')))
    
    if len(pessoas) == 0:
        maior = menor = listaAux[1]
    elif listaAux[1] > maior:
        maior = listaAux[1]
    elif listaAux[1] < menor:
        menor = listaAux[1]
    
    pessoas.append(listaAux[:])
    print(pessoas)
    listaAux.clear()
    escolha = str(input('Deseja adicionar mais pessoas? [S/N]'))


print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg. de:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menor} Kg. de:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
        