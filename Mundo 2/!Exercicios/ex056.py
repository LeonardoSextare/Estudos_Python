#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadeAux = int(0)
media = int(0)
mulheres = int(0)
homem = str()

for c in range(1, 5):
    nome = (str(input(f'Qual o nome da {c}° pessoa?? ')))
    idade = (int(input(f'Qual a idade da pessoa?? ')))
    sexo = (str(input(f'Qual o gênero da pessoa? F - Feminino ou M - Masculino '))).strip().lower()
    
    media += idade
    
    if sexo == 'f' or sexo == 'feminino':
        if idade < 20:
            mulheres +=1
    elif sexo == 'm' or sexo =='masculino':
        if idade > idadeAux:
            homem = nome
            idadeAux = idade
          
media = media/c

print(f'O homem mais velho tem {idadeAux} e se chama: {homem}\nA média da idade do grupo é de: {media}\n{mulheres} mulher(es) possuem idade menor que 20 anos')
