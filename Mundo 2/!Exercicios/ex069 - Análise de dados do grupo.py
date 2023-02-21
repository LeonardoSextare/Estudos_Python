# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = idadecont = homems = mulheres = 0

while True:
    cont += 1
    print('===== Cadastro de Pessoas =====')
    idade = int(input(f'Qual a idade da {cont}° Pessoa a ser cadastrada?\n>>> '))
    if idade > 18: # Adiciona +1 ao contador de +18
        idadecont += 1
    
    # Pergunta e Valida o sexo da pessoa
    sexo = ' '
    while sexo not in 'fm': 
        sexo = str(input(f'Qual o gênero da pessoa?[F/M]\n>>> ')).lower().strip()[0]
        if sexo not in ('fm'):
            print('Opção Invalida.')
    
    if sexo == 'm': # Adiciona +1 ao contador de homems
        homems += 1
    else:
        if idade < 20: # Adiciona +1 ao contador de mulheres com -20
            mulheres += 1
            
    while True: # Pergunta se deseja cadastrar mais uma pessoa e faz a validação da resposta
        escolha = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).lower().strip()[0]
        if escolha == 's':
            escolha = ''
            break
        elif escolha == 'n':
            escolha = 'n'
            break
        else:
            print('Opção Invalida.')
            
    if escolha == 'n': # Encerra o programa se a reposta for não
        break
    
print(f'Você cadastrou um total de {cont} pessoas!\nPessoas com mais de 18 anos: {idadecont}\nHomens Cadastrados: {homems}\nMulheres com menos de 20 anos: {mulheres}')