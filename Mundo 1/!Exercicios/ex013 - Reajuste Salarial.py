#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input('Digite o salario atual do funcionario: \n'))

print('O novo salario dele será de: R$ {:.2f}' .format(salario*1.15))