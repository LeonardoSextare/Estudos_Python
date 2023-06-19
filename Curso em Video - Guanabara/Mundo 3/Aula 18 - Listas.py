#Listas em listas = Matrizes
listas = [['Pedro',    19], 
          ['Leonardo', 22], 
          ['João',     44]]

# print(listas)
# print(listas[1])
# print(listas[1][1])
# print(listas[1][0][0])

# listas.append(['Roberto', 29])
# listas.append('Maria')
# print(listas)
# print(listas[4])

teste = [] #Cria uma lista vazia
teste2 = list() # Declara a variavel como lista
teste.append(listas) #Cria uma ligação igualmente o =
teste2.append(listas[:]) #Cria uma copia
teste2[0][0] = ['Teste', 19]
print(teste)
print(teste2)

