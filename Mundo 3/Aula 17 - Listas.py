# Declarar uma lista (array)

array = []  # Vazio

array = [1, 2, 3, 4, 5]  # Com Valores

print(array)
print(array[3])

array.append(10)  # Adiciona o elemento na ultima posição
print(array)

array.insert(0, 'Cu')  # Adiciona no indice 0 o parametro dps da virgula
print(array)

del array[4]  # Deleta o indice 4
array.pop(4)  # Deleta o indice 4

if 'Cu' in array:  # Verifica se o valor passado está na lista
    array.remove('Cu')  # Remove o valor da lista

array.pop()  # Elimina o ultmo elemento da lista

valores = list(range(4, 11))  # list() cria uma lista

valores.sort()  # Ordena os valores

valores.sort(reverse=True)  # Ordena os valores na ordem reversa

print(len(valores)) #Retorna quantos elementos estão na lista

for i,v in enumerate(valores):
    print(i,v)
    

a = [1,2,3,4]
b = a # vincula o B ao A, se mudar o B o A muda e vice-versa = [:] não vincula, somente passa os valores
print(a)
print(b)
b[2] = 6
print(a)
print(b)
