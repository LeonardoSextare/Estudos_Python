nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome == '' or idade == '':
    print('Você deixou campos vazios')
else:
    print(f'Seu nome é {nome}!')
    print(f'Seu nome invertido: {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome possui espaços!')
    else:
        print(f'Seu nome não possui espaços!')

    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')