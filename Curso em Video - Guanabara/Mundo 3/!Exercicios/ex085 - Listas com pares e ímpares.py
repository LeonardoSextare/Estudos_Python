#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
nAux = int()
for c in range(0,7):
    nAux = int(input(f'Digite o {c+1} número: '))
    if nAux%2 == 0:
        numeros[0].append(nAux)
    else:
        numeros[1].append(nAux)

numeros[0].sort()
numeros[1].sort()
print(f'O números pares digitados foram: {numeros[0]}')
print(f'O números ímpares digitados foram: {numeros[1]}')