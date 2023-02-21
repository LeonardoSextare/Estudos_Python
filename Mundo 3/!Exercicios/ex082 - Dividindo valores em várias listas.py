#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
impar = []
par = []

escolha = 's'

while escolha != 'n':
    numeros.append(int(input('Digite um número inteiro: ')))
    escolha = str(input('Quer continuar? [S/N]'))[0].lower()

for c in numeros:
    if c%2 == 0:
        par.append(c)
    else:
        impar.append(c)
        
print(f'Lista principal: {numeros}')
print(f'Números pares digitados: {par}')
print(f'Números ímpares digitados: {impar}')
