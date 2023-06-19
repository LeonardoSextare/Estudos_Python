#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar.

dinheiro = float(input('Digite quantos Reais(R$) você tem e saiba quantos Dolares(US$) você pode comprar: \n'))

print('Cotação do Dolar Atual 28/12/2022 \nR$ 1,00 = US$ 5,27')
print('Você tem R$ {} e pode comprar US$ {:.2f}' .format(dinheiro, dinheiro/5.27))
