numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número: {numero} é Par!')
    else:
        print(f'O número: {numero} é Impar!')   

except:
    print(f'"{numero}" não é um número inteiro!')
