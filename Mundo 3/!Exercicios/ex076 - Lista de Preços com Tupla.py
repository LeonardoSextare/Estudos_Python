#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = ('Notebook Gamer', 4499.99,
          'Monitor Full HD', 999,
          'Processador Intel', 700,
          'Processador AMD', 600,
          'Placa Mãe LGA 1700', 600,
          'Placa Mãe AM4', 700,
          'Cooler CPU', 99,
          'Pasta Térmica Prata 50g', 49 
          )

print(50*'=' + f'\n{"Tabela de Preços":^50}\n' + 50*'=')

for c in range(0,len(tabela),2):
    print(f'{tabela[c]:.<39}'+f'R$ {tabela[c+1]:>7.2f}')
