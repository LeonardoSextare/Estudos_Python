perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 10*10?',
        'Opções': ['10', '1000', '100', '110'],
        'Resposta': '100',
    },
]

venceu = 0

for pergunta in perguntas:
    print(f'\nPergunta: {pergunta["Pergunta"]}\n')

    for indice, valor in enumerate(pergunta["Opções"]):
        print(f'{indice}) {valor}')

    escolha = int(input('Escolha uma opção:'))
    if pergunta["Opções"][escolha] == pergunta["Resposta"]:
        print('Acertou!!')
        venceu += 1
    else:
        print('Errou!')

print(f'Você acertou {venceu}\nde {len(perguntas)} perguntas')