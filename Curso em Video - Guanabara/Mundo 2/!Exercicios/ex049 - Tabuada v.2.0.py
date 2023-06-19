#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um Numero para saber sua tabuada: \n'))

print(f'A tabuada do numero {num} é')
for c in range(0,11):
    print(f'{num} X {c:2} = {num*c:2}')