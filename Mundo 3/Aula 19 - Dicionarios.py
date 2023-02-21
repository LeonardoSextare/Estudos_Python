# Declarar um dicionario

pessoa = {}  # Declara um dicionario vazio
pessoa = dict()  # Declara um dicionario vazio

# Declara a variavel com valores preenchidos
pessoa = {'nome': 'Leonardo', 'idade': 22}
print(pessoa['idade'], pessoa['nome'])

pessoa['sexo'] = 'M'  # Cria um novo valor sexo no dicionario
print(pessoa)

del pessoa['idade']  # Deleta o valor idade do dicionario
print(pessoa)

print(pessoa.values())  # Exibe somente os valores do dicionario

print(pessoa.keys())  # Exibe as chaves

print(pessoa.items())  # Exibe as chaves e os valores delas no dicionario

for c, v in pessoa.items():  # Percorre as chaves e valores em items no dicionario
    print(f'o {c} é {v}')

# Uma lista com index numerais e em cada index possui um dicionario
pessoas = [{'nome': 'Leonardo', 'idade': 22}, 
           {'nome': 'Pedro', 'idade': 55},
           {'nome': 'Roberto', 'idade': 99}]

print(pessoas)
print(pessoas[0]['nome'])
print(pessoas[2]['nome'])

pessoas.append(pessoa.copy()) # Copia o dicionario para a lista, sem criar relação

  