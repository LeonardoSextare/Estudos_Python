nome = input('Digite seu primeiro nome: ')

nome_comprimento = len(nome)


if not nome:
    print('Nome em Branco')
elif nome_comprimento < 4:
    print('Seu nome é curto!')
elif nome_comprimento in range(5,7):
    print('Seu nome é normal!')
elif nome_comprimento > 6:
    print('Seu nome é muito grande')


