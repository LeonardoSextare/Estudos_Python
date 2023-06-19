#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = [str(input('Digite a expressão'))]

abre = fecha = 0

for i in range(0,len(expressao[0])):
    if expressao[0][i] == ')':
        fecha += 1
    elif expressao[0][i] == '(':
        abre +=1
    
    if fecha > abre:
        print('Expressão inválida!')
        break

if abre == fecha:
    print('Expressão válida!')
    