#Tuplas são parecidas como vetores, porém são imutaveis durante a execução ou seja, não podem ser alteradas.


# Declaração de Tupla

lanches = ('Hamburguer', 'Sorvete', 'Suco', 'Pudim')
print(lanches)

print(lanches[1]) # Exibe o sorvete pois em tuplas o 0 conta

print(lanches[-3]) #Funciona ao contrario também

print(lanches[0:2]) # Printa 2 elementos começando pelo 0, ou seja ele mostra do 0 ao 1 total 2 elementos

#lanches[1] = 'Refrigerante' #como tuplas são imutaveis esse comando não funciona.

for comida in lanches:
    print(f'Vou comer {comida}')
    
for contador in range (0, len(lanches)):
    print(f'Vou comer {lanches[contador]}')
    
for comida in enumerate(lanches):
    print(f'Vou comer {comida}')
    
    
print(sorted(lanches))