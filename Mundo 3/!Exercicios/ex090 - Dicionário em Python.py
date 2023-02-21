#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Nome: ').capitalize())
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno['média'] < 7:
   aluno['situação'] = 'Recuperação'
else:
    aluno['situacão'] = 'Reprovado'

print('='*40)
for i, c in aluno.items():
    print(f'{i} é igual a {c}')