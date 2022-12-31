#Faça um programa que leia a largura e a altura de uma parede em metros e calcula a sua área e quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2metros quadrados

largura = float(input('Digite a largura da parede em metros: \n'))
altura = float(input('Digite a altura da parede em metros: \n'))

print('Você precisa de {} Litros de tinta para pintar a parede!' .format((largura*altura)/2))