lista = []
while True:
    while True:
        escolha = input('Selecione uma opção:\n[i]nserir, [a]pagar, [l]istar, [s]air\n>>')[0].lower()
        if escolha not in 'ial':
            print('Opção Invalida.')
            continue
        break

    if escolha == 'i':
        valor = input('Qual valor você quer inserir?')
        lista.append(valor)

    elif escolha == 'a':
        if len(lista) == 0:
            print('Lista Vazia, impossivel apagar.')
        else:
            print(f'Lista:')
            for indice, valor in enumerate(lista):
                print(indice, valor)

            try:
                valor = int(input('Digite o indice do valor você quer apagar:'))
                lista.pop((valor))
            except ValueError:
                print('Digite somente números.')
            except IndexError:
                print('Indice Invalido')

    elif escolha == 'l':
        if len(lista) == 0:
            print('Lista Vazia')
        else:
            print(f'Lista:')
            for indice, valor in enumerate(lista):
                print(indice, valor)

    elif escolha == 's':
        print('Encerrando Programa...')
        break
