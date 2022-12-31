#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: \n')).strip().lower()

print(f"""A letra "A" foi digitada {frase.count('a')} vezes
Apareceu pela primeira vez na posição: {frase.find('a')+1}
Apareceu pela ultima vez na posição: {frase.rfind('a')+1}""")
