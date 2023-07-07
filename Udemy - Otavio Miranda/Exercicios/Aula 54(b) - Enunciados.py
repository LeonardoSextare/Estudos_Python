hora_atual = input('Informe a hora atual: ')

try:
    hora_atual = int(hora_atual)

    if hora_atual in range(0, 12):
        print('Bom dia !')
    elif hora_atual in range(12, 18):
        print('Boa tarde!')
    elif hora_atual in range(18, 24):
        print('Boa noite!')
    else:
        print('Horario Invalido!')

except:
    print(f'O valor "{hora_atual}" não é um número!')
