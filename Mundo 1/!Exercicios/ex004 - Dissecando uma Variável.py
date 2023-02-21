#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = (input('Digite qualquer coisa e saiba informações sobre ele'))

print('O tipo primitivo do valor digitado é : ', type(algo))
print('Só possui espaços?', algo.isspace())
print('É um numero?', algo.isnumeric())
print('É alfabetico?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está somente maiúsculo?', algo.isupper())
print('Está somente minúsculo', algo.islower())
print('Está capitalizada?', algo.istitle())

#.is existem varias formas de testar uma string e ver o que está digitado nela de forma simples
# exemplo de uso string.isnumeric() testa se a string está escrito somente caracteres numericos