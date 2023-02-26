# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

num = float(input('Digite um valor para receber informações: R$ '))

print(f'Valor acrescido 10%: R${aumentar(num,10):.2f}')
print(f'Valor decrescido 15%: R$ {diminuir(num, 15):.2f}')
print(f'O dobro de R$ {num:2.2f} é: R$ {dobro(num):.2f}')
print(f'A metade de R$ {num:2.2f} é: R$ {metade(num):.2f}')