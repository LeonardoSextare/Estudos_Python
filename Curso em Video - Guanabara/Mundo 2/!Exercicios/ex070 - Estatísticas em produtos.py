# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
totalCompra = tot1000 = barato = 0
produtoBarato = str()
while True:
    produto = str(input('Qual é nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$ '))
    
    if barato == 0 or preco < barato:
        barato = preco
        produtoBarato = produto
    
    totalCompra += preco
    if preco >= 1000:
        tot1000 += 1
    
    continuar = ' '
    while continuar not in ('sn'):
        continuar = str(input('Você deseja cadastrar outro produto? [S/N]')).lower().strip()[0]
        if continuar not in ('sn'):
            print('Opção Invalida')
    if continuar == 'n':
        break

print(f'Valor total da compra: R$ {totalCompra}\nProdutos que custam mais de R$ 1000: {tot1000}\nProduto mais barato: {produtoBarato} custando R$ {barato}')