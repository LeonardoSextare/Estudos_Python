#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

num = float(input('Digite um valor para receber informações: R$ '))

print(f'Valor acrescido 10%: {moeda.aumentar(num,10, True)}')
print(f'Valor decrescido 15%: {moeda.diminuir(num, 15, True)}')
print(f'O dobro de {moeda.moeda(num)} é: {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é: {moeda.metade(num, True)}')