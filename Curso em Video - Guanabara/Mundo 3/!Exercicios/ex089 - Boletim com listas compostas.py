# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
aux = []

escolha = 's'
while escolha != 'n':
    aux.append(str(input('Aluno: ')).capitalize())
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    
    aluno.append(aux[:])
    aux.clear()
    
    escolha = str(input('Deseja cadastrar outro aluno? [S/N] '))
print(30*'='+ '\nNum. Nome            Média\n' + 30*'=')
for i in range(0, len(aluno)):
    print(f'{i}    {aluno[i][0]:<10} {(aluno[i][1]+aluno[i][2])/2:>9}')

while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 p/ Finalizar) '))
    if escolha == 999:
        break
    print(f'As notas de {aluno[escolha][0]} são {aluno[escolha][1:]}')
    
print('Finalizando...\nVolte Sempre!')