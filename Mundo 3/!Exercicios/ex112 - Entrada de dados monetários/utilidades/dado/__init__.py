# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

def leiaDinheiro(msg):
    
    while True:
        saida = input(str(msg)).strip().replace(',','.')
        if saida.replace('.','').isnumeric():
            break
        print(f'ERRO! {saida} não é um número')
    saida = float(saida)
        
    return saida