# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Velocidade da pista: 80 Km/h\nInsira a velocidade do carro analisado: '))

if velocidade > 80:
    print(f'MULTADO! A multa será de R$: {float((velocidade - 80)*7):.2f}')
else:
    print(f'Velocidade Normal')