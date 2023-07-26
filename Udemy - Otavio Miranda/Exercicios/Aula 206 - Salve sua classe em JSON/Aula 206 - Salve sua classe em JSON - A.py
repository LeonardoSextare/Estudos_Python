import json


class Pessoa:

    def __init__(self, nome, idade, altura, peso, sexo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo


p1 = Pessoa('Leonardo', 22, 1.71, 65, 'Masculino')
p2 = Pessoa('Pedro', 23, 1.81, 120, 'Masculino')
p3 = Pessoa('Brenda', 28, 1.68, 65, 'Feminino')

dados = [vars(p1),vars(p2),vars(p3)]

with open('classe_pessoa.json', 'w', encoding='utf8') as a:
    json.dump(dados, a, ensure_ascii=False, indent=2)


print(*dados, sep='\n', end='\n\n')
