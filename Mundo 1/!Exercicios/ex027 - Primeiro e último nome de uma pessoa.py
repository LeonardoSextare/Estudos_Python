# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: \n')).strip().title()

print(f'Seu primeiro nome é: {nome[:nome.find(" ")]}\nSeu ultimo nome é: {nome[nome.rfind(" ")+1:]}')
