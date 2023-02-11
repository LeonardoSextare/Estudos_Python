# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

palavra = str(input('Digite uma palavra ou frase e verifique se ela é palíndromo:\n> ')).upper().strip()
invertido = str()

palavra2 = palavra.replace(' ', '')
for c in range(len(palavra2)-1, -1, -1):
   # invertido = f'{invertido}'+ f'{palavra2[c]}'
    invertido += palavra2[c]
print(f'O inverso de {palavra} é {invertido}')
if invertido == palavra2:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
print(invertido)