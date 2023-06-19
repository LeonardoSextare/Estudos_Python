# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from modulo import *

num = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi: {num}')

num = leiaFloat('Digite um número decimal: ')
print(f'O número digitado foi: {num}')