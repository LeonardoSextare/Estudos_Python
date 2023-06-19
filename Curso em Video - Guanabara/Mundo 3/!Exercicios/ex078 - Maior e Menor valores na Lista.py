# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
historico = int()
for c in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {c}: ')))

print(f'O maior número foi: {max(valores)} na posição ', end='')
for c in range(0, len(valores)):
    if valores[c] == max(valores):
        print(f'{valores.index(valores[c],historico)}', end='...')
        historico = c+1

historico = int()
print(f'\nO menor número foi: {min(valores)} na posição ', end='...')
for c in range(0, len(valores)):
    if valores[c] == min(valores):
        print(f'{valores.index(valores[c], historico)}', end='...')
        historico = c+1
