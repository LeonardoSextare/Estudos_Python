# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidades import dado, moeda
num = dado.leiaDinheiro('Digite um valor para receber informações: R$ ')

print(moeda.resumo(num, 20, 30))

