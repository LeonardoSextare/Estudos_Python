#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete','Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(-1)
    while num not in range(0,len(extenso)):
        num = int(input('Digite um número de 0 a 20 para saber seus nome por extenso:\n>>> '))
        
    print(f'O número {num} por extenso é: {extenso[num]}')
    
    answer = str(input('Deseja saber outro número? [S/N]\n>>> '))[0]
    if answer in 'nN':
        break