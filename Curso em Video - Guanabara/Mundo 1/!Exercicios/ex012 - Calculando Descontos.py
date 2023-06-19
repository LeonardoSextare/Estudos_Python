#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto para aplicar 5%'' de desconto:' ))

print('Preço original do produto: R$ {:.2f}\nPreço com desconto:        R$ {:.2f}' .format(preco, preco-(preco*0.05)))