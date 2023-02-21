#   Crie um programa que leia o nome completo de uma pessoa e mostre:– O nome com todas as letras maiúsculas e minúsculas.
#   O nome com todas as letras maiúsculas e minúsculas.
#   Quantas letras ao todo (sem considerar espaços).
#   Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print('Seu nome com letras maiuscula: {}\nSeu nome com letras minusculas: {}'.format(nome.upper(),nome.lower()))
print('Seu nome tem {} letras!\nSeu primeiro nome é {} e tem {} letras!'.format(len(''.join((nome.split()))),nome.split()[0] ,len(nome.split()[0])))
