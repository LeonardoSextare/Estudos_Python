a =  (2, 5, 4)
b =  (5, 4, 8, 2)
c = a + b # Ele junta as tuplas e não soma elas
print(c)

print(c.count(4)) # Ele conta quantas vezes o numero 4 aparece em c

print(c.index(2)) # Ele mostra a posição do número indicado na tupla e só mostra a primeira ocorencia
print(c.index(4, 3)) # Mostra a posição da primeira aparição do 4, mas só começa a procurar depois do index 4

del(a) #Apaga uma variavel durante a execução do programa, inclusive apaga tuplas tbm