nome = 'Leonardo'

tamanho_nome = len(nome)
novo_nome = str()
contador = 0
while contador < tamanho_nome:
    novo_nome += '*' + nome[contador] 
    contador+= 1

print(novo_nome)