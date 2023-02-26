# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

num = float(input('Digite um valor para receber informações: R$ '))

print(f'Valor acrescido 10%:{moeda.moeda(moeda.aumentar(num,10))}')
print(f'Valor decrescido 15%: {moeda.moeda(moeda.diminuir(num, 15))}')
print(f'O dobro de {moeda.moeda(num)} é: {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é: {moeda.moeda(moeda.metade(num))}')