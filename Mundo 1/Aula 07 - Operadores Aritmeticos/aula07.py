n1 = int(input('Digite um Número: '))
n2 = int(input('Digite outro Número: '))
nome = input('Qual seu nome?')

print('O operador de soma é: "+" Exemplo: {} + {} = {}' .format(n1, n2, n1+n2))
print('O operador de subtração é: "-" Exemplo: {} - {} = {}' .format(n1, n2, n1-n2))
print('O operador de multiplicação é: "*" Exemplo: {} * {} = {}' .format(n1, n2, n1*n2))
print('O operador de divisão é: "/" Exemplo: {} / {} = {}' .format(n1, n2, n1/n2)) ## Limitar casas depois do . = nas chaves/mascara utilizar .xf x = numeros de casas, semelhante a linguagem C
print('O operador de potenciação é: "**" Exemplo: {} ** {} = {}' .format(n1, n2, n1**n2))
print('O operador de divisão inteira é: "//" Exemplo: {} // {} = {}' .format(n1, n2, n1//n2))
print('O operador de resto da divisão é: "%" Exemplo: {} % {} = {}' .format(n1, n2, n1 % n2))
print('Raiz Quadrada de {} é igual a: {}' .format(n1, n1**(1/2)))
print('Raiz Cubica de {} é igual a: {}' .format(n1, n1**(1/3)))
# Raiz Quadrada ou Cubica de um numero pode ser feito forçando uma divisão antes

# 1 = ()
# 2 = **
# 3 = * ou / ou // ou %% - Quem aparecer primeiro da esquerda para direita
# 4 = + ou - Quem aparecer primeiro da esquerda para direita

print('Oi' + 'Oi')
print(' Oi' * 5)
print(' Oi'*20)
print ('formatação de string em mascara: caracteres minimos {:20}, alinhado a direita ou esquerda{:<}, centralizado {:^}, preenchimento de espaços vazios {:=^20} ' .format(nome, nome, nome, nome))


