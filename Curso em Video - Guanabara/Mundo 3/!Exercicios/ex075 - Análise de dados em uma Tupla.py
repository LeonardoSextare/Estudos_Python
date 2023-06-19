# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
cont = int()
pares = int()

print(f'Número de vezes que o 9 foi digitado: {numeros.count(9)}')
if 3 in numeros:
    print(f'Aonde aparece o 3 pela primeira vez: {numeros.index(3)+1} ')
else:
    print('Número 3 não encontrado')


for c in range(0,len(numeros)):
    if (numeros[c])%2 == 0:
        pares += 1
print(f'Números pares digitado: {pares}')