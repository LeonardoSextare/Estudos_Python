# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Digite os comprimentos de um triangulo e veja se pode formar um triangulo:')
n1 = float(input('Digite o Comprimento 1:'))
n2 = float(input('Digite o Comprimento 2:'))
n3 = float(input('Digite o Comprimento 3:'))

if n1 < (n2 + n3) and n2 < (n1+n3) and n3 < (n1 + n2):
    print('Podem Formar um Triangulo!')
else:
    print('Não Podem Formar um Triangulo!')
    