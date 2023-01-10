# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime
ano = int(input(
    'Informe um ano e saiba se ele é bissexto:\n(Digite 0 para analisar o ano atual) \n'))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
