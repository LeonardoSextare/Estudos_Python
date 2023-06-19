#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
escolha = 's'
while escolha != 'n':
    lista.append(int(input('Digite um número inteiro: ')))
    escolha = str(input('Você quer continuar?? [S/N]'))[0].lower()
    print(lista)

lista.sort(reverse=True)
print('===== Informações da Lista =====')
print(f'Foram digitados {len(lista)} números')
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')