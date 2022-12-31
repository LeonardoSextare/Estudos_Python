#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome de seu cidade: ')).strip()


print(f'O nome da sua cidade é {cidade}.\nComeça com SANTO? {cidade[:5].lower() == "santo"}')

