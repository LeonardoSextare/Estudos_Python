# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus = float(input('Digite a temperatura em °C: '))

print('A temperatura de {}°C equivale a {} °F!' .format(graus, (graus*9/5)+32))
