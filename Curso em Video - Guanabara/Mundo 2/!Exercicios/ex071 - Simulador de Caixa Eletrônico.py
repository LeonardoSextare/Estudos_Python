# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedula50 = cedula20 = cedula10 = cedula1 = 0
print ('='*36 + f'\n{"Banco Sextare":^36}\n' + '='*36)

valorSaque = int(input('Qual é o valor do saque? R$ '))

while valorSaque >= 50:
    cedula50 += 1
    valorSaque -= 50
    
while valorSaque >= 20:
    cedula20 += 1
    valorSaque -= 20
    
while valorSaque >= 10:
    cedula10 += 1
    valorSaque -= 10
    
while valorSaque >= 1:
    cedula1 += 1
    valorSaque -= 1

print(f'Informações do Saque:\n{cedula50} Notas de R$ 50\n{cedula20} Notas de R$ 20\n{cedula10} Notas de R$ 10\n{cedula1} Notas de R$ 1')
print('='*36+ '\nVolte sempre!')