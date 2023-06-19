# Para criar uma função utilizar
def criarfuncao():
    print('teste')


# é possivel passar um parametro através de uma variavel na função
def mensagem(msg):
    print(20*'=-')
    print(msg)
    print(20*'=-')


mensagem('Teste') #Utilizando a função passando parametros

def soma(n1, n2):
    print(f'n1 = {n1} e n2 = n2 = {n2}')
    s = n1 + n2
    print(f'A soma de N1 + N2 = {s}')


soma(n2 = 2, n1 = 5) #Definindo valores passando os parametros explicitos

soma(2, 3)

def contador (*n): # Recebe n valores e guarda em uma tupla
 for c in n:
     print(c) # Podemos trabalhar com as tuplas livremente
    
contador(1,2,3,4,5,6,7)

#Podemos passar listas para uma função
listaTeste = [1,2,3,4,5,6,7,8]

def listas(teste):
    for c in teste:
        print(c)
        
listas(listaTeste)