# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
teste = 0
def area(n1, n2):
    area = n1 * n2
    print(f'A área de um terreno {n1}x{n2} é igual a {area}m²')

print(f'Controle de Terrenos\n' + 20*'=')

area(float(input('LARGURA (m):')), float(input('COMPRIMENTO (m):')))
