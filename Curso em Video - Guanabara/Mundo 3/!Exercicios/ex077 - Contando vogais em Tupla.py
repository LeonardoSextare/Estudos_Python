#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Teste', 'Edificio', 'Desenvolvedor', 'Hardware', 'Software')
vogais = ('A', 'E', 'I', 'O', 'U')

for c in range(0,len(palavras)):
    print(f'A palavra {palavras[c]} tem as vogais: ', end='')
    
    for x in vogais:
        if x in palavras[c].upper():
            print((x+' ')*palavras[c].upper().count(x), end= '')
    print()