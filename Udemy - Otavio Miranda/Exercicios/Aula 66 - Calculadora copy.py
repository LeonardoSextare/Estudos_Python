

while True:
    num1 = float(input('Escolha um número:'))
    num2 = float(input('Escolha outro número:'))
    print('Escolha a operação a ser realizada:\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Novos Números\n')
    operacao = int(input('>'))
    if operacao == 1:
        resultado = num1 + num2
        operador = '+'
    elif operacao == 2:
        resultado = num1 - num2
        operador = '-'
    elif operacao == 3:
        resultado = num1 * num2
        operador = '*'
    elif operacao == 4:
        resultado = num1 / num2
        operador = '/'
    elif operacao == 5:
        resultado = 0
        operador = ''
        continue
    else:
        print('Opção Invalida')

    print(f'{num1} {operador} {num2} = {resultado}')
    escolha = input('Realizar nova operação??[S/N]')[0]
    if escolha in 'Nn':
        break
