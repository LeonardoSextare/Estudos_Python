#help() no console para entrar no modo de ajuda, ensina como utilizar comandos e bibliotecas
#quit ele sai no modo help
a = 10
#print(input.__doc__) # Outra forma, porém mais simples de obter ajuda sobre um comando

def somar (n1,n2,n3=0): # n3=0 define que o n3 é opcional
    global a
    a = 5
    soma = n1 + n2 + n3
    #print(f'Soma total {soma}')
    return soma
    
a = somar(1,2) #Retorna o valor de soma para variavel a

print(a)