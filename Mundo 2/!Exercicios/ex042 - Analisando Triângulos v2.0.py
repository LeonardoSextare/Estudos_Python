# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('Digite os comprimentos de um triangulo e veja se pode formar um triangulo:')
n1 = float(input('Digite o Comprimento 1:'))
n2 = float(input('Digite o Comprimento 2:'))
n3 = float(input('Digite o Comprimento 3:'))

if n1 < (n2 + n3) and n2 < (n1+n3) and n3 < (n1 + n2):
    print('Podem Formar um Triangulo', end='')
    if n1 == n2 == n3:
        print(' EQUILÁTERO')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print(' ISÓSCELES')
    else:
        print(' ESCALENO')
else:
    print('Não Podem Formar um Triangulo!')
 