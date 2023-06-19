# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print(f'A média do aluno foi de : {media}')

if media >= 5 and media <= 6.9:
    print('O aluno está de recuperação!')
elif media < 5:
    print('O aluno foi reprovado')
else:
    print('O aluno foi aprovado!')
