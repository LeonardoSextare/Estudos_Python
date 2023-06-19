# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

escolha = 's'
while escolha != 'n':
    nAux = int(input('Digite um valor para adicionar a lista:'))
    if nAux not in numeros:
        numeros.append(nAux)
    else:
        print('Número Repetido! Ignorado.')

    escolha = str(input('Quer adicionar mais números? [S/N]'))[0].lower()

numeros.sort()
print(f'Os números escolhidos foram: {numeros}')
