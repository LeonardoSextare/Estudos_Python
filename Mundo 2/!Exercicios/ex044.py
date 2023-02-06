# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('Calculadora de Pagamento')
valor = float(input('Insira o valor total do produto:\nR$'))

tipo = int(input('Digite a forma de pagamento:\n1 - A vista/cheque\n2 - A vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais no cartão\nEscolha: '))

if tipo == 1:
    print(f'Valor total do produto a vista no dinheiro/cheque: R${valor*0.9100:.2f}')
    
elif tipo == 2:
    print(f'Valor total do produto a vista no cartão: R${valor*0.95:.2f}')
    
elif tipo == 3:
    print(f'Valor total do produto parcelado 2x no cartão: R${valor}')
    print(f'Quantidade de parcelas: 2\nValor da parcela R${valor/2}')
    
elif tipo == 4:
    parcela = int(input('Quantas parcelas será a compra??'))
    print(f'Valor total do produto parcelado no cartão em 3x ou mais: R${valor*1.20}')
    print(f'Quantidade de parcelas: {parcela}\nValor da parcela R${(valor*1.20)/parcela}')
    
else:
    print('Opção Invalida')