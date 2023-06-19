import random

qnt_gerador = int(input("Quantos CPF's você quer gerar??"))

for c in range(qnt_gerador):

    # Gerador dos nove digitos iniciais
    nove_digitos = str()
    for c in range(0, 9):
        nove_digitos += str(random.randint(0, 9))

    # Gerando o penultimo digito
    soma_cpf = 0
    for i in range(10, 1, -1):
        soma_cpf += i*int(nove_digitos[-i+1])

    penultimo_digito = (soma_cpf * 10) % 11
    if penultimo_digito > 9:
        penultimo_digito = 0
    
    cpf = f'{nove_digitos}{penultimo_digito}'
    
    # Gerando o ultimo digito
    soma_cpf = 0
    for i in range(10, 1, -1):
        soma_cpf += i*int(cpf[-i+1])

    ultimo_digito = (soma_cpf * 10) % 11
    if ultimo_digito > 9:
        ultimo_digito = 0
    
    cpf = f'{nove_digitos}{penultimo_digito}{ultimo_digito}'
    
    print(cpf)

