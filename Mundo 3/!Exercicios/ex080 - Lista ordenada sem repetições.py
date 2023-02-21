#  Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []
nAux = int()
for i in range(0, 5):
    while True: #Filtro de números repetidos
        nAux = int(input(f'Digite o {i+1}° número:'))
        if nAux not in numeros:
            break
        else:
            print('Número repetido, tente novamente!')
            
    # Primeira entrada
    if i == 0 or nAux > max(numeros):
        numeros.append(nAux)
        print('Adicionado ao final da Lista')
    
    else: # Se não for o maior nem menor, compara com cada elemento e o seu posterior, se verdadeiro inseri no meio
        for i in range(0, len(numeros)):
            if nAux > numeros[i] and nAux < numeros[i+1]:
                numeros.insert(i+1, nAux)
                print(f'Adicionado a posição {numeros.index(nAux)}')
          
print(f'Os números adicionados foram: {numeros}')
