# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
trabalhador = {}
ano = date.today().year

trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = ano - nasc
ctps = int(input('Carteira de trabalho [0 - Não Possui]: '))

if ctps == 0:
    trabalhador['ctps'] = 'não possui'
else:
    trabalhador['ctps'] = ctps
    
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = int(input('Salário: R$ '))
    trabalhador['aposentadoria'] = (35 + trabalhador['contratação']) - ano + trabalhador['idade']

print(f'{" Informações ":=^40}')
for k, c in trabalhador.items():
    print(f'- {k} é igual a {c}')