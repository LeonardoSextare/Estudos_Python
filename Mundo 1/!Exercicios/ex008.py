#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Digite um valor em metros para converter em centimentros e milimetros:\n'))

print('Valor Digitado: {}m\nCentimetros: {}cm\nMilimetros: {}mm' .format(metros, metros*100, metros*1000))

##Desafio Extra
print('Kilometros: {}\nHectometro: {}\nDecametro: {}\nDecimetros: {}'.format(metros/1000,metros/100,metros/10,metros*10))