import json

dados_classe = []

with open('classe_pessoa.json', 'r', encoding='utf8') as a:
    dados_classe = json.load(a)


class Pessoa:

    def __init__(self, nome, idade, altura, peso, sexo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo

p1 = Pessoa(**dados_classe[0])
p2 = Pessoa(**dados_classe[1])
p3 = Pessoa(**dados_classe[2])

print(*p1.__dict__.items(), *p2.__dict__.items(), *p3.__dict__.items(), sep='\n', end='\n\n')
print()
print(*dados_classe, sep='\n', end='\n\n')
