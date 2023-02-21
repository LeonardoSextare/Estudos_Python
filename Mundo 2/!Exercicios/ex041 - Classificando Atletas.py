# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

import time

idade = time.localtime().tm_year - int(input('Informe o ano de nascimento do atleta: \n'))

print(f'O Atleta tem {idade} anos.')

if idade <= 9 :
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFATIL')
elif idade <= 19:
 print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')

