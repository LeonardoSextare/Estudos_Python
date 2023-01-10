# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Fore.GREEN + """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
=             Simulador de Emprestimos            =
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")


casa = float(input('Qual o valor da casa que deseja comprar? \n' + Fore.LIGHTGREEN_EX + 'R$'))
salario = float(input(Style.RESET_ALL + 'Qual seu salario mensal?\n' + Fore.LIGHTGREEN_EX + 'R$'))
parcelas = int(input(Style.RESET_ALL + 'Em quantos anos deseja pagar?\n' + Fore.LIGHTCYAN_EX))*12
print(Style.RESET_ALL)

valorParcela = casa/parcelas
print(f'Uma casa no valor de R${casa:.2f} em {parcelas/12:.0f} anos terá a prestação de R${valorParcela:.2f}')
if valorParcela > salario*0.30:
    print(Fore.LIGHTRED_EX + 'Emprestimo Negado!')
else:
    print(Fore.LIGHTGREEN_EX + 'Emprestimo Aprovado')
