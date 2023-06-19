#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('Digite o seu gênero: M - Masculino ou F - Feminino')

genero = str()
while genero != 'f' and genero != 'm':
    genero = input('Digite seu gênero:').lower()[0]
    
    if genero != 'f' and genero != 'm':
        print('Opção invalida. Digite somente M ou F')

if genero == 'm':
    genero = 'Masculino'
elif genero == 'f':
    genero = 'Feminino'
print(f'O genero digitado foi: {genero}')
    